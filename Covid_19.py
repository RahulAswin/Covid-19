from covid import Covid
import subprocess
import sys

covid=Covid()

print("\nCOVID - 19 INFORMATION\n")
print("1 . Information Of Covid-19 in World")
print("2 . Information Of An Particular Country")
print("3 . Get All Data(188 Countries)")
print("4 . Install Covid Package\n")

a=int(input("Enter Any Option : "))

if a==1 :
    print("\nTotal No Of Active Cases : ",covid.get_total_active_cases())
    print("Total No Of Confirmed Cases : ",covid.get_total_confirmed_cases())
    print("Total No Of Deaths : ",covid.get_total_deaths())
    print("Total No Of Recovered Persons : ",covid.get_total_recovered())

elif a==2:
    a=input("Enter a Country Name : ")
    b=covid.get_status_by_country_name(a)
    data={
        key : b[key]
        for key in b.keys() and {'confirmed',
                                'active',
                                'deaths',
                                'recovered'}
    }
    print("\nIn",a,"there are ",)
    print(data)    

elif a==3:
    b=covid.get_data()
    for x in b:
        print(x)
elif a==4:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "covid"])
