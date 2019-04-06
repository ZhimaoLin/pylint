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
            # print(f.value.func.name)
            self.function_dic[node.name].append(f.value.func.name)
        # self.function_dic
        # if node.name == 'main':
        #     print(node.repr_tree())
        #     print(node.body[1].repr_tree())

    def print_call_graph(self, dic, f_name, tab_count):
        print(tab_count*"\t" + f_name + "()")
        if f_name in dic:
            for f in dic[f_name]:
                    self.print_call_graph(dic, f, tab_count+1)

    def close(self):
        if 'main' in self.function_dic:
            self.print_call_graph(self.function_dic, "main", 0)
def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(CallGraph(linter))