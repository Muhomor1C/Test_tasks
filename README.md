
   1/ Напишите функцию, которая на вход принимает строку, 
состоящую из строчных и заглавных латинских символов, а возвращает 
кортеж из двух элементов: символа, который встречается в строке чаще
всего (без учета регистра!), и числа вхождений этого символа в строку.
Если таких символов несколько, функция должна вернуть любой из них.
Например, для строки "aaaAAAbc" результатом работы функции будет
('a', 6).

   get_most_character_example 1-2
   
   2/ Напишите функцию, которая на вход принимает единственное целое
число N, а возвращает целый квадратный корень из этого числа, если
такой существует, или None, если такого корня нет. Нельзя использовать
функцию sqrt() из модуля math для извлечения квадратного корня.

   extract_sqrt
    
   3/ Напишите функцию, которая принимает на вход строку, состояющую
из символов '(' и ')', задающих скобочную последовательность, и
возвращает True, если последовательность корректна, иначе False.

   checking_brackets
