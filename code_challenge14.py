anime_list = []

while True:
    anime = input("Enter the title of an anime (or type 'exit' to finish): ").strip().lower()
    
    if anime == 'exit':
        print("\nYou have exited the anime entry program.")
        break
    
    anime_list.append(anime)
    print(f"'{anime}' has been added to your anime list.\n")

print("Your anime list includes:")
for a in anime_list:
    print(f"- {a}")
