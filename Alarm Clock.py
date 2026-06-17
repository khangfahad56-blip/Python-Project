import time
import datetime

#Function which Show Main Menu

def menu():
    print("****************************")
    print("     Python Alarm Clock     ")
    print("****************************")
    print("1: Current Time")
    print("2: Set Alarm")
    print("****************************")

#Function which show the Current Time and Give it in "Hr:Min:Sec"(String) Format

def get_current_time():

    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Your Current time is {current_time}")
    return current_time

#Function Which take Time for User and Give it in "Hr:Min:Sec"(String) Format
def get_alarm_time():

    try:

        while True:

            user_time_sec = int(input("Write the Time in Second: "))

            if user_time_sec > 60 or user_time_sec < 0:
                print("Second can't be greater then 60 or lesser then 0")
                continue

            else:
                break

        while True:

            user_time_min = int(input("Write the Time in Minute: "))

            if user_time_min > 60 or user_time_min < 0:
                print("Minute can't be greater then 60 or lesser then 0")
                continue

            else:
                break

        while True:

            user_time_hrs = int(input("Write the Time in Hour: "))

            if user_time_hrs < 0:
                print("Hour can't be greater then 60 or lesser then 0") 
                continue 

            else:
                break

    except TypeError:

        print("You Wrote an Ivalid Value Type")

    except Exception:

        print("Opps! Something went wrong")

    user_time = (f"{user_time_hrs}:{user_time_min:02}:{user_time_sec:02}")
    return user_time

#Main Body of Code in main()

def main():

    menu()

    while True:
        
        try:

            option = float(input("Choice a Option (1-2): "))
            
            if option == 1:
                get_current_time()

            elif option == 2:
                
                user_time = get_alarm_time()

                while True:

                    if datetime.datetime.now().strftime("%H:%M:%S") >= user_time:
                        print("Alarm Time is Up")
                        break
                    else:
                        get_current_time()
                        time.sleep(1)
                        continue
            else:
                print("Type a Number Blw 1 or 2.")

        except ValueError:
            print("You Wrote an Ivalid Value Type")
            continue

        except Exception:
            print("Something When Wrong")
            continue

#Good practice When you want to transfer code to another Project
if __name__ == "__main__":
    main()