age=float(input("Enter the age of your child : "))
if age>=4.0:
    print("Congratulation Your Child got the admission")
elif age>=3.5:
    print("Congratulation Your Child got the admission But But But! Your child is not eligible for Nursery\nChild will spend some months in montessior")
else:
    wait=4-age
    print("You should shame, Your child is not eligible for the admission,You should wait for ",wait," Years")