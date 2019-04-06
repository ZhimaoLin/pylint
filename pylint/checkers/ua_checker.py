import astroid

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class UaCmput174Checker(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'ua-cmput174'
    priority = -5
    msgs = {
        'R0011': (
            'No main function.',
            'no-main-function',
            'Program should include a user-defined parameterless function called main.'
        ),
        'C0012': (
            'Main function is not the first one.',
            'main-function-not-first',
            'Main function should be the first function in the python file.'
        ),
        'R0013': (
            'Main function is not called.',
            'main-function-is-not-called',
            'Program should call main function.'
        ),
        'E0014': (
            'Main function is called more than once.',
            'main-function-is-called-multiple-times',
            'Program should call main function only once.'
        ),
        'C0061': (
            'Use a constant multiple times.',
            'duplicated-constants',
            'Please define a const'
        ),
        'C0062': (
            'Constant assignments are too far away from its parent.',
            'constant-assignment-far',
            'Please assign constants closed to its parent'
        ),
        'C0071': (
            'Adjacent duplicate code.',
            'adjacent-duplicate-code',
            'The program has 2 adjacent lines with the same code'
        ),
        'C0074': (
            'User-defined function have more than 12 statement.',
            'user-defined-function-have-more-than-12-statement',
            'User-defined function should have less than 12 statement..'
        ),
    }
    options = (
        (
            "ua-max-statements",
            {
                "default": 12,
                "type": "int",
                "metavar": "<int>",
                "help": "Maximum number of statements in function / method " "body.",
            }
        ),
        (
            "allowed_duplicate_constant",
            {
                "default": ("", 0, 0.0, 1, -1, 2),
                "type": "csv",
                "metavar": "<allowed duplicated constants>",
                "help": "These constants are allowed to be duplicated",
            },
        ),
        (
            "ua-max-dist-const-assign-and-parent",
            {
                "default": 5,
                "type": "int",
                "metavar": "<int>",
                "help": "Maximum distance between a constant assignment and its parent.",
            },
        ),
    )

    def __init__(self, linter=None):
        super(UaCmput174Checker, self).__init__(linter)
        self.is_there_a_main_function = False
        self.is_there_a_main_function_node = None
        self.function_count = 0

        self.main_function_is_called = False
        self.main_function_called_count = 0

        self.constant_list = []


        self._function_stack = []

    def visit_functiondef(self, node):
        self.function_count += 1
        if (not self.is_there_a_main_function) and node.name == 'main':
            self.is_there_a_main_function = True
            if self.function_count != 1:
                self.add_message('main-function-not-first', node=node)

        if len(node.body) > self.config.ua_max_statements:
            self.add_message('user-defined-function-have-more-than-12-statement', node=node)

        for i in range(0, len(node.body)-1):
            if node.body[i].as_string() == node.body[i+1].as_string():
                self.add_message('adjacent-duplicate-code', node=node)


        # self._function_stack.append([])

    def leave_functiondef(self, node):
        # print('leave function def')
        pass

    def visit_const(self, node):
        if node.value in self.config.allowed_duplicate_constant:
            return
        if node.value in self.constant_list:
            self.add_message('duplicated-constants', node=node)
        else:
            self.constant_list.append(node.value)




    def visit_assign(self, node):
        if not type(node.value) is astroid.node_classes.Const:
            return

        if node.lineno - node.parent.lineno > self.config.ua_max_dist_const_assign_and_parent:
            self.add_message('constant-assignment-far', node=node)



    def visit_call(self, node):

        if type(node.func) is astroid.node_classes.Attribute:
            return

        if node.func.name and node.func.name == 'main':
            self.main_function_called_count += 1
            self.main_function_is_called = True

            if self.main_function_called_count > 1:
                self.add_message('main-function-is-called-multiple-times', node=node)


    def visit_return(self, node):
        # print('visit return')
        pass



    def close(self):
        if self.is_there_a_main_function == False:
            self.add_message('no-main-function')
        if self.main_function_is_called == False:
            self.add_message('main-function-is-not-called')


def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(UaCmput174Checker(linter))