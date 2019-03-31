import turtle

class LSystem:

    def __init__(self, start_string='', iterations=1, rules_dict={}, measures_dict={}, fn_dict={}):
        self.rules_dict = rules_dict
        self.state_string = start_string
        self.iterations = iterations
        self.fn_dict = fn_dict

    def set_rules_dict(self, rules_dict):
        self.rules_dict = rules_dict

    def display(self, turtle1=turtle.Pen()):
        for _ in range(0, self.iterations):
            self.__apply_rules()
        self.__draw_turtle_fn(self.fn_dict, turtle1)

    def __apply_rules(self):
        new_state = ''
        for char in self.state_string:
            translated_chars = self.rules_dict[char] if char in self.rules_dict else char
            new_state = new_state + translated_chars
        self.state_string = new_state

    def __draw_turtle_fn(self, fn_dict, turtle1):
        for char in self.state_string:
            if char in fn_dict:
                fn = fn_dict[char]
                fn(turtle1)

    def end_this(self):
        turtle.done()

if __name__ == '__main__':
    rules_dict={'F':'F-F++F-F'}
    start_string='F'
    measures_dict = {'length':2, 'angle':60}
    fn_dict = {'F':lambda turtle1: turtle1.forward(measures_dict['length']), 
            'B':lambda turtle1: turtle1.backward(measures_dict['length']),
            '-':lambda turtle1: turtle1.left(measures_dict['angle']),
            '+':lambda turtle1: turtle1.right(measures_dict['angle']),}

    ls = LSystem(start_string=start_string, rules_dict=rules_dict, iterations=4, fn_dict=fn_dict)
    ls.display()
    ls.end_this()