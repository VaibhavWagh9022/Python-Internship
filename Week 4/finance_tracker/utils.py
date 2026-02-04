def safe_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nOperation cancelled")
        return None
