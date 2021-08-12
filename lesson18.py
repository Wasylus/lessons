import json


with open("example.json") as json_file:
    data: dict = json.load(json_file)

    # Explicit, longer
    # glossary: dict = data["glossary"]
    # book: dict = data["book"]
    # title: str = glossary["title"]

    # Minimized
    print(data["glossary"].get("title"))
    print(data["book"].get("title"))
    # print(json.dumps(data, indent=4, sort_keys=True))

    # Minimized
    try: 
        book_title = data["book"]["titla"]
    except KeyError as e:
        print(f"Something went wrong! {e}") 
    except Exception as e:
        print("General exception class", e)
    else:
        print("Everything went fine!")
    finally:
        print("But we always run this block")
    # except Exception as e:
    #     print("General exception class", e)
    # except:
    #     print("General exception class")

from typing import Optional, List

def get_age(some_string: str) -> Optional[float]:
    # try casting to int, then return it
    # if there's an error, return 0 and print warning message
    try:
        return int(some_string)
    except ValueError:
        print("unable to cast this value")
        return None
    # else:
    #     print("Yay!")
    #     return as_int
        

age = input("What's your age?")
print(get_age(age))

# print(data)
# def turtle_bar(number: int) -> bool:
#     if number >= 200:
#         return redd