import astroid

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

SPACE = '    '

class CallGraph(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'call-graph'
    priority = 0
    msgs = {
        'R9999': (
            'Call graph',
            'call-graph-message',
            'Draw a call graph'
        ),
    }
    options = ()

    def __init__(self, linter=None):
        super(CallGraph, self).__init__(linter)
        self.function_dic = {}
   
    def visit_functiondef(self, node):
        self.function_dic[node.name] = []
        for f in node.body:
            # print(f.repr_tree())
            # print(type(f))
            self.function_dic[node.name].append(f)


    def print_assign(self, node, tab_count):
        for target in node.targets:
            if type(node.value) is astroid.node_classes.Call:
                print(tab_count*SPACE + target.as_string() + ' = ' + node.value.as_string())

    def print_aug_assign(self, node, tab_count):
        if type(node.value) is astroid.node_classes.Call:
            print(tab_count*SPACE + node.target.as_string() + ' ' + node.op + ' ' + node.value.as_string())

    def print_loop(self, node, tab_count):
        if type(node) is astroid.node_classes.For:
            print(tab_count*SPACE + "for loop: ")
        elif type(node) is astroid.node_classes.While:
            print(tab_count*SPACE + "while loop: ")
        for b in node.body:
            self.print_call_graph(b, tab_count)

    def print_if(self, node, tab_count):
        print(tab_count*SPACE + 'if True')
        for b in node.body:
            self.print_call_graph(b, tab_count)

        print(tab_count*SPACE + 'else False')
        for b in node.orelse:
            self.print_call_graph(b, tab_count)

    def print_try_except(self, node, tab_count):
        print(tab_count*SPACE + 'try: ')
        for b in node.body:
            self.print_call_graph(b, tab_count)

        for handler in node.handlers:
            if handler.type:
                print(tab_count*SPACE + "except " + handler.type.name + ":")
            else:
                print(tab_count*SPACE + "except: ")
            
            for b in handler.body:
                self.print_call_graph(b, tab_count)

    def print_try_final(self, node, tab_count):
        for b in node.body:
            self.print_call_graph(b, tab_count-1)
        
        for f in node.finalbody:
            print(tab_count*SPACE + "finally: ")
            self.print_call_graph(f, tab_count)

    # Only this function handles tab_count logic
    def print_call_graph(self, node, tab_count):
        if type(node) is astroid.node_classes.Assign:
            self.print_assign(node, tab_count+1)
        elif type(node) is astroid.node_classes.AugAssign:
            self.print_aug_assign(node, tab_count+1)
        elif (type(node) is astroid.node_classes.For) or (type(node) is astroid.node_classes.While):
            self.print_loop(node, tab_count+1)
        elif type(node) is astroid.node_classes.If:
            self.print_if(node, tab_count+1)
        elif type(node) is astroid.node_classes.TryExcept:
            self.print_try_except(node, tab_count+1)
        elif type(node) is astroid.node_classes.TryFinally:
            self.print_try_final(node, tab_count+1)
        elif type(node) is astroid.node_classes.Expr:

            if type(node.value) is astroid.node_classes.Call:

                if node.value.func.name in self.function_dic:
                    print((tab_count+1)*SPACE + node.value.func.name + "()")
                    for item in self.function_dic[node.value.func.name]:
                        self.print_call_graph(item, tab_count+1)
                else:
                    print((tab_count+1)*SPACE + node.value.as_string())
        else:
            pass
            
    def close(self):
        print('==============================')
        print('|         Call Graph         |')
        print('==============================')
        if 'main' in self.function_dic:
            print('main()')
            for item in self.function_dic['main']:
                self.print_call_graph(item, 0)

def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(CallGraph(linter))