print("welcome to boook my show!")

theater_name=input("enter the name of the theater (pvr,inox):")

if theater_name =="pvr" or theater_name=="inox":
    if theater_name =="pvr":
        print("\n MOvies available at pvr :")
        MOvies1="Avatar : the way of water"
        MOvies2="the batman"
        ticket_price1=900
        ticket_price2=800
    else:
        print("\n movies available at inox:")
        MOvies1="Mission:impossible"
        MOvies2="Jurassic park"
        ticket_price1=900
        ticket_price2=950

    print(f"1.{MOvies1}")
    print(f"1.{MOvies2}")

    movie_choice = input("\n enter the number to your chosen movie (1 or 2):")

    if movie_choice == "1" or movie_choice =="2":
        if movie_choice =="1":
            selected_movie=MOvies1
            ticket_price = ticket_price1
        else:
            selected_movie = MOvies2
            ticket_price = ticket_price2

        print(f"\n you have selected : {selected_movie}")
        print(f"ticket price : RS {ticket_price}")


        confirmation = input("\n Do you want to confirm the booking ? (yes/no):")

        if confirmation =="yes":
            print(f"\n ticket for '{selected_movie}' has been booked sucussfully")
        else:
            print("\n ticket booking has been cancelled")
    else:
        print("invalid movie choice.please try agian")
else:
    print("sorry,the threater name is not available")