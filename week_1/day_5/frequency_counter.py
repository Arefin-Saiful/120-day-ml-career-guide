def main():
    text = "banana"
    freq = {}
    
    for char in text:
        # Check if hash address is empty or occupied
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            
    print(f"Frequencies: {freq}")

if __name__ == "__main__":
    main()