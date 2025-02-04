


class CalcException(Exception):
    pass

def input_data():
    arg1 = input("print number>>> ")
    arg2 = input("print second number>>> ")
    action = input("action>>> ")
    return arg1, arg2, action


def check_data(arg1, arg2, action):
    try:
        if "." in arg1:
            arg1 = float(arg1)
        else:
            arg1 = int(arg1)
    except ValueError:
        raise CalcException("Error arg1")

    try:
        if "." in arg2:
            arg2 = float(arg2)
        else:
            arg2 = int(arg2)
    except ValueError:
        raise CalcException("Error arg2")

    if action not in ["+","-","*","/"]:
        raise CalcException("Error arg1")

    return arg1, arg2, action

def output_data(arg1, arg2, action):
    if action == "+":
        print(arg1+arg2)
    elif action == "-":
        print(arg1-arg2)
    elif action == "*":
        print(arg1*arg2)
    elif action == "/":
        print(arg1/arg2)


if __name__ == '__main__':
    m_arg1, m_arg2, m_action = input_data()
    try:
        m_arg1, m_arg2, m_action = check_data(m_arg1, m_arg2, m_action)
    except CalcException as e:
        print(e)
        exit(1)
    output_data(m_arg1, m_arg2, m_action)
