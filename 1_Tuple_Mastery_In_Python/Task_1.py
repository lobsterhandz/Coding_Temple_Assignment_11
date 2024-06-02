def format_itineraries(itineraries):
    result = ""  # Initialize an empty string to hold the result
    index = 1  # Start the index at 1
    for itinerary in itineraries:  # Loop through each itinerary in the list
        traveler_name = itinerary[0]  # Get the traveler's name
        origin = itinerary[1]  # Get the origin
        destination = itinerary[2]  # Get the destination
        # Format the string for the current itinerary
        formatted_string = f"Itinerary {index}: {traveler_name} - From {origin} to {destination}\n"
        result += formatted_string  # Add the formatted string to the result
        index += 1  # Increment the index for the next itinerary
    return result  # Return the final result

# Example usage
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_result = format_itineraries(itineraries)
print(formatted_result)
