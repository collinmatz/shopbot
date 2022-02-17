from LinkClass import Link
from LinkCollectionClass import LinkCollection
import requests

def main():
    # commands list
    commands = [
        ["_EXIT", "Terminates program"],
        ["_NEWLINK", "Establishes a new link to track"],
        ["_UPDATELINK", "Updates a currently existing link"],
        ["_DELLINK", "Deletes a currently existing link"]
    ]

    print("Welcome to ShopBot! Type _COMMANDS to get started!")

    linkCollection = LinkCollection()
    running = True
    while (running):
        command = input(">>>  ")
        
        if command == "_COMMANDS":
            for command in commands:
                print(command[0], command[1])
        elif command == "_EXIT":
            running = False
        elif command == "_NEWLINK":
            url = input("Please insert the URL you would like to track: ")
            try:
                response = requests.get(url)
            except:
                print("Error with establishing link connection. Please try again.")
            else:
                newLink = Link(url)
                linkCollection.addLink(newLink)
                print("Done! You are now tracking", newLink.getUrl(), "as one of your links!")
        elif command == "_UPDATELINK":
            print("Please specify the link you would like to update:")
        elif command == "_GETLINKS":
            linkCollection.printLinks()

if __name__ == "__main__":
    main()