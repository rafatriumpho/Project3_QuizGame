quiz = [
    {'question': 'Quem foi o primeiro homem criado por Deus?', 'answer': 'Adão'},
    {'question': 'Quem foi a esposa de Adão?', 'answer': 'Eva'},
    {'question': 'Quem construiu a arca?', 'answer': 'Noé'},
    {'question': 'Qual profeta liderou Israel para fora do Egito?', 'answer': 'Moisés'},
    {'question': 'Qual mar Moisés abriu?', 'answer': 'Mar Vermelho'},
    {'question': 'Quem derrotou Golias?', 'answer': 'Davi'},
    {'question': 'Qual era o nome do filho da promessa de Abraão?', 'answer': 'Isaque'},
    {'question': 'Quem foi vendido como escravo pelos irmãos e depois se tornou governador no Egito?', 'answer': 'José'},
    {'question': 'O que Deus criou no primeiro dia?', 'answer': 'Luz'},
    {'question': 'Qual mandamento diz para honrar pai e mãe?', 'answer': 'Quinto mandamento'}
]
score = 0

print ('\nWelcome to the Quiz game! Answer the questions and see how much of the Old Testament you know.')
for q in quiz:
     user_answer = input('\n' + q['question'] + '\n')
     if user_answer.lower() == q['answer'].lower():
         print ('Correct!')
         score += 1
     else:
         print (f"Wrong, the answer is {q['answer']}.")

print (f"Your total score was {score}/10")
if score == 10:
     print ('Exellent! You know the Old Testament very well!')
elif score >= 8:
     print ('Good job!')
elif score >= 5:
     print ('Not bad, but you should study more!')
else:
     print ('You should study more!')
