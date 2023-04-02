import sys
import json
import doctest

class Adventure():
    def __init__(self, mapPath):
        self.map = json.load(open(mapPath))
        self.current_room = 0
        self.inventory = []
        self.verbs = {'go': 1, 'look': 0, 'get': 1, 'drop': 1, 'inventory': 0, 'help': 0, 'quit': 0}

    def has_items(self):
        return self.map[self.current_room].get('items') != None and len(self.map[self.current_room].get('items')) > 0

    def go(self, direction):
        if not direction:
            sys.stdout.write("Sorry, you need to 'go' somewhere.\n")
        elif direction in self.map[self.current_room]['exits'].keys():
            self.current_room = self.map[self.current_room]['exits'][direction]
            sys.stdout.write("You go " + direction + ".\n\n")
            self.look()
        else:
            sys.stdout.write(f"There's no way to go " + direction + ".\n")

    def look(self):
        if self.has_items():
            sys.stdout.write(f"> {self.map[self.current_room]['name']}\n\n{self.map[self.current_room]['desc']}\n\nItems: {', '.join(self.map[self.current_room]['items'])}\n\nExits: {' '.join(self.map[self.current_room]['exits'].keys())}\n\n")
        else:
            sys.stdout.write(f"> {self.map[self.current_room]['name']}\n\n{self.map[self.current_room]['desc']}\n\nExits: {' '.join(self.map[self.current_room]['exits'].keys())}\n\n")
    
    def get(self, item):
        if not item:
            sys.stdout.write("Sorry, you need to 'get' something.\n")
        elif not self.has_items():
            sys.stdout.write(f"There's no {item} anywhere.\n")
        elif item in self.map[self.current_room]['items']:
            self.inventory.append(item)
            self.map[self.current_room]['items'].remove(item)
            sys.stdout.write(f'You pick up the {item}.\n')
        else:
            sys.stdout.write(f"There's no {item} anywhere.\n")

    def drop(self, item):
        if not item:
            sys.stdout.write("Sorry, you need to 'drop' something.\n")
        elif item in self.inventory:
            self.inventory.remove(item)
            if not self.has_items():
                self.map[self.current_room]['items'] = []
            self.map[self.current_room]['items'].append(item)
            sys.stdout.write(f"You drop the {item}.\n")
        else:
            sys.stdout.write(f"You're not carrying the {item}.\n")

    def show_inventory(self):
        if len(self.inventory) > 0:
            inventory = '\n  '.join(self.inventory)
            sys.stdout.write(f"Inventory:\n  {inventory}\n")
        else:
            sys.stdout.write("You're not carring anything.\n")

    def help(self):
        commands = ""
        for verb in self.verbs.keys():
            if self.verbs[verb] == 1:
                commands += '  ' + verb + '...\n'
            else:
                commands += '  ' + verb + '\n'
        sys.stdout.write("You can run the following commands:\n" + commands)
    

    def run(self):
        self.look()
        while(True):
            # winning and losing conditions
            if self.current_room == 4: # win
                if 'sword' in self.inventory and 'shield' in self.inventory:
                    sys.stdout.write("You encountered a dragon and defeated it with your sword and shield! You won! Congratulations!🎇\n")
                    break
                else: # lose
                    sys.stdout.write("You encountered a dragon but were defeated due to a lack of weapons. You lose. Try again!\n")

            # read the input
            try:
                action_input = input("What would you like to do? ")
                action = action_input.strip().lower().split()
            except EOFError:
                sys.stdout.write("\nUse 'quit' to exit.\n")
                continue
            if len(action) == 2:
                verb = action[0]
                target = action[1]
            elif len(action) == 1:
                verb = action[0]
                target = None
            else:
                sys.stdout.write(f"Sorry, '{action_input}' is not defined. You can run 'help' to view available commands.\n")
                continue

            # perform actions
            if verb == 'go':
                self.go(target)
            elif verb == 'look' and target == None:
                self.look()
            elif verb == 'get':
                self.get(target)
            elif verb == 'drop':
                self.drop(target)
            elif verb == 'inventory'and target == None:
                self.show_inventory()
            elif verb == 'help' and target == None:
                self.help()   
            elif verb == 'quit':
                sys.stdout.write("Goodbye!\n")
                break
            else:
                sys.stdout.write(f"Sorry, '{action_input}' is not defined. You can run 'help' to view available commands.\n")



if __name__ == "__main__": 
    assert len(sys.argv) == 2
    mapPath = str(sys.argv[1])
    adventure = Adventure(mapPath)
    adventure.run()