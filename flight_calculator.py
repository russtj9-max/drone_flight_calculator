#calc start
print("Flight calculator started")
#Flight time method
def calculate_flight_time(weight_grams):
    #If grams weight is negative, raise an error
    if weight_grams < 0:
        raise ValueError("A negative weight is not possible.")
    #Here Copilot guessed a formula for flight that was not correct because it made up a weight.
    #Implements the flight time calculation i recieved with a minor change that is still right.
    #Here Copilot correctly determined that i wanted the weight_grams divided by 10 (Or multiplied by 0.1) so i pushed with no changes.
    fTime = 180 - (weight_grams / 10)
    #Sets fTime to 0 when it goes negative
    if fTime < 0:
        fTime = 0
    #Returns the calculated flight time
    return fTime

#Method to return a list of weights and their corresponding flight times incrementing by step_grams
def flight_time_table(max_weight_grams, step_grams):
   #Declare and initialize the current weight and the list to store flight times
   currWeight = 0.0
   weightFlightTimes = []  # List to store each [weight, flight_time] pair, Attempted with a double array, failed testing because the array would start with two empty slots, i implemented it wrong, copilot reverted back to single array.
   #Loop through weights and calculate flight times
   while currWeight <= max_weight_grams:
       weightFlightTimes.append([currWeight, calculate_flight_time(currWeight)])
       #Iterate by step grams
       currWeight += step_grams  # Copilot formula correctly guessed i wanted step grams, I shortened to += for efficiency.
   #Returns the list of weights and their corresponding flight times.
   return weightFlightTimes