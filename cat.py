# Hannalore Morrow
# 2/10/2024
# CS 361_400

# Dictionary to store cat breeds and their attributes
cat_breeds = {
    "Bengal": {"Weight": "8-18 lbs", "Personality": "Energetic, affectionate, adventurous", "Energy": "High"},
    "British Shorthair": {"Weight": "9-18 lbs", "Personality": "Easygoing, calm, devoted", "Energy": "Medium"},
    "Maine Coon": {"Weight": "10-25 lbs", "Personality": "Playful, adaptable, friendly", "Energy": "Medium"},
    "Norwegian Forest cat": {"Weight": "8-20 lbs", "Personality": "Adaptable, laid-back, independent", "Energy": "Medium"},
    "Persian": {"Weight": "7-14 lbs", "Personality": "Sweet, gentle, quiet", "Energy": "Low"},
    "Ragdoll": {"Weight": "10-20 lbs", "Personality": "Loving, laid-back, sweet", "Energy": "Medium"},
    "Scottish Fold": {"Weight": "5-13 lbs", "Personality": "Sweet, loving, undemanding", "Energy": "Medium"},
    "Siamese": {"Weight": "7-13 lbs", "Personality": "Loving, entertaining, vocal", "Energy": "High"},
    "Siberian": {"Weight": "10-20 lbs", "Personality": "Affectionate, playful, intelligent", "Energy": "High"},
    "Sphynx": {"Weight": "6-12 lbs", "Personality": "Loving, outgoing, demanding", "Energy": "High"}
}

def search_by_name(name):
    if name in cat_breeds:
        return cat_breeds[name]
    else:
        return "Breed not found."

# Displays breed information
def display_breed_info(breed_info):
    print("Breed Information:")
    for key, value in breed_info.items():
        print(f"{key}: {value}")

# Search by description
def search_by_description(description):
    found_breeds = []
    for breed, attributes in cat_breeds.items():
        if description.lower() in attributes["Personality"].lower():
            found_breeds.append(breed)
    return found_breeds

# Lists possible search traits
def list_search_traits():
    all_traits = set()
    for breed_info in cat_breeds.values():
        for trait in breed_info["Personality"].split(', '):
            all_traits.add(trait.lower())  # Convert to lowercase 
    print("Searchable Traits For Cat Breeds:")
    for trait in sorted(all_traits):
        print(trait.capitalize())  # Capitalize first letter 


# Displays the source of information
def display_source():
    print("Source of Information: https://www.litter-robot.com/blog/breeds-of-cats/")

def main():
    while True:
        print("\nWelcome to the Cat Breed Search!")
        print("1. Search by breed name")
        print("2. Search by personality description")
        print("3. Lists searchable personality traits")
        print("4. Display source of information")
        print("5. Exit")

        choice = input("Please select an option: ")

        if choice == "1":
            breed_name = input("Enter the breed name: ")
            result = search_by_name(breed_name)
            if result != "Breed not found.":
                display_breed_info(result)
            else:
                print(result)
        elif choice == "2":
            personality_description = input("Enter a personality description: ")
            result = search_by_description(personality_description)
            if result:
                print("Breeds matching the description:", ', '.join(result))
                choice = input("Would you like more information about a breed? (Y/N): ")
                if choice.lower() == "y":
                    breed_name = input("Enter the breed name: ")
                    if breed_name in result:
                        display_breed_info(cat_breeds[breed_name])
                    else:
                        print("Invalid breed name.")
            else:
                print("No breeds found matching the description.")
        elif choice == "3":
            list_search_traits()
        elif choice == "4":
            display_source()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
