#import Calc as Cc

#m_arg1, m_arg2, m_action = Cc.input_data()
#try:
#    m_arg1, m_arg2, m_action = Cc.check_data(m_arg1, m_arg2, m_action)
#except Cc.CalcException as e:
#    print(e)
#    exit(1)
#Cc.output_data(m_arg1, m_arg2, m_action)
#print(dir(Calc))
from Calc import input_data

a, b, c = input_data()
print(a, b, c)
