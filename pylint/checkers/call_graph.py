import astroid

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class CallGraph(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'call-graph'
    priority = -6
    msgs = {
        'C9999': (
            'User-defined function have more than 12 statement.',
            'call-graph-message',
            'User-defined function should have less than 12 statement..'
        ),
    }
    options = (
        (
            "max-depth",
            {
                "default": 12,
                "type": "int",
                "metavar": "<int>",
                "help": "Maximum number of statements in function / method " "body.",
            }
        ),
    )

    def __init__(self, linter=None):
        super(CallGraph, self).__init__(linter)
        self.function_dic = {}
        

    def visit_functiondef(self, node):
        self.function_dic[node.name] = []
        for f in node.body:
            # print(f.repr_tree())
            # print(type(f))
            self.function_dic[node.name].append(f)
            # if type(f) is astroid.node_classes.Expr:
            #     self.function_dic[node.name].append(f)
            # elif type(f) is astroid.node_classes.While:
            #     self.function_dic[node.name].append(f)
            # elif type(f) is astroid.node_classes.For:
            #     self.function_dic[node.name].append(f)

    def print_assign(self, node, tab_count):
        for target in node.targets:
            print(tab_count*'\t' + target.as_string() + ' = ' + node.value.as_string())

    def print_loop(self, node, tab_count):
        if type(node) is astroid.node_classes.For:
            print(tab_count*"\t" + "for loop: ")
        else:
            print(tab_count*"\t" + "while loop: ")
        for b in node.body:
            # self.print_call_graph(self, f_name, tab_count)
            if type(b) is astroid.node_classes.Expr:
                self.print_call_graph(b.value.func.name, tab_count+1)
            elif (type(b) is astroid.node_classes.For) or (type(b) is astroid.node_classes.While):
                self.print_loop(b, tab_count+1)




    def print_call_graph(self, f_name, tab_count):
        print(tab_count*"\t" + f_name + "()")

        # Deal with build in functions
        if f_name not in self.function_dic:
            return

        for f in self.function_dic[f_name]:
            if type(f) is astroid.node_classes.Assign:
                self.print_assign(f, tab_count+1)
            
            elif (type(f) is astroid.node_classes.For) or (type(f) is astroid.node_classes.While) :
                self.print_loop(f, tab_count+1)

            # if type(f) is astroid.node_classes.Expr:
            #     self.print_call_graph(f.value.func.name, tab_count+1)
            

    
            
    def close(self):
        if 'main' in self.function_dic:
            self.print_call_graph("main", 0)

def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(CallGraph(linter))