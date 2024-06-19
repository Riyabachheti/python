# Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
def check_prefix_suffix(string, prefix, suffix):
    starts_with_prefix = string.startswith(prefix)
    ends_with_suffix = string.endswith(suffix)
    
    print(f"String: {string}")
    print(f"Starts with '{prefix}': {starts_with_prefix}")
    print(f"Ends with '{suffix}': {ends_with_suffix}")

# Example usage
input_string = input("Enter the string ")
prefix = input("Enter the prefix ")
suffix = input("Enter the suffix ")

check_prefix_suffix(input_string, prefix, suffix)
