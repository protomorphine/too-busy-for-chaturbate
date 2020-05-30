import os
from classes.Model import Model
from classes.Vidak import Vidak


def main():
    try:

        welcome_logo = open("wellcome.txt", "r").read()
        os.system("cls")
        print(welcome_logo)

        model = Model(input("Please, enter model nickname:\n> "))

        if model.connect_to_chaturbate():
            model.get_m3u8_link()
            vidak = Vidak(model)
            vidak.record_m3u8_stream()
        else:
            print("Model with nickname " + model.nickname + " doesn't exist.")
            print("Please check nickname and try again.")

    except KeyboardInterrupt:
        print("Script was stopped by user. Exiting.")


if __name__ == "__main__":
    main()
