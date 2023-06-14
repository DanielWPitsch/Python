# aprendendo yield
#Perceba, o yield nesse código funciona mais ou menos como um return,
#entretanto, mantém salvo o contexto da função, e quando o for()
#de dentro do main itera novamente, a função gen_squares_in_interval()
#volta a ser chamada, continuando sua execução de onde parou, mantendo
#o contexto da sua iteração, seguindo a sequência correta do range(x, y).

def other_math(number):
  print('do the math with:', number)
  
def gen_squares_in_interval(x, y):
  for i in range(x, y):
    yield i*i

if __name__ == '__main__':

  x, y = (10, 20)
  
  for number in gen_squares_in_interval(x, y):
    other_math(number)
