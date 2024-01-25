def is_between_200_and_500(number):
   if number>200 and number<500:
       result = "Yes"
   else:
       result= "No"
   return result 
    

number = 5

#call the is_between_200_and_500 function
final_result = is_between_200_and_500(number)
print(final_result)