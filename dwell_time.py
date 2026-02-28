import pandas as pd

# PARAMETERS
FILE_PATH = "data/OD_MAGENTA_Janak Puri West to Botanical Garden.xlsx"
BUS_CAPACITY = 40
BOARDING_TIME_PER_PASSENGER = 3.5
STANDEE_MULTIPLIER = 4
ALIGHTING_TIME_PER_PASSENGER = 2
DOOR_TIME = 4

def calculate_dwell_times():
    """
    Calculates the dwell time at each transit stop based on boarding and alighting data,
    accounting for capacity constraints and standee penalties using global parameters.
    """
    # Read data
    df = pd.read_excel(FILE_PATH)
    df['Stop'] = pd.to_numeric(df['Stop'], errors='coerce').fillna(0).astype(int)
    
    stop_ids = df['Stop'].tolist()
    boarding = df['Boarding'].tolist()
    alighting = df['Alighting'].tolist()

    onboard_passengers = 0
    boarding_times = []
    alighting_times = []
    total_dwell_time =[]

    for i in range(len(stop_ids)):
        # Passengers alight 
        onboard_passengers -= alighting[i]
        if onboard_passengers < 0:
            onboard_passengers = 0

        alighting_time = alighting[i] * ALIGHTING_TIME_PER_PASSENGER
        alighting_times.append(alighting_time)

        # Passengers board
        passengers_after_boarding = onboard_passengers + boarding[i]
        
        # Calculate boarding time with standee penalty
        if passengers_after_boarding > BUS_CAPACITY: 
            standees = passengers_after_boarding - BUS_CAPACITY 
            if standees >= boarding[i]:                
                boarding_time = boarding[i] * STANDEE_MULTIPLIER # All new boarders are standees
            else:                
                boarding_time = (boarding[i] - standees) * BOARDING_TIME_PER_PASSENGER + (standees * STANDEE_MULTIPLIER) # Some get seats, some stand
        else:            
            boarding_time = boarding[i] * BOARDING_TIME_PER_PASSENGER # Everyone gets a seat

        onboard_passengers = passengers_after_boarding
        boarding_times.append(boarding_time)

        # Total Dwell Time (Boarding + Alighting + Door Open/Close Time)
        dwell_time = boarding_time + alighting_time + DOOR_TIME
        total_dwell_time.append(dwell_time)

    # Create Output DataFrame
    dwell_times_df = pd.DataFrame({
        "Stop": stop_ids,
        "Alighting": alighting,
        "Boarding": boarding,
        "Boarding Time (sec)": boarding_times,
        "Alighting Time (sec)": alighting_times,
        "Dwell Time (sec)": total_dwell_time
    })

    return dwell_times_df

if __name__ == "__main__":
    results_df = calculate_dwell_times()
    
    if results_df is not None:
        print("##### Transit stop dwell time calculation results #####")
        print(results_df.to_string(index=False))
        print(f"\nMaximum Dwell Time: {results_df['Dwell Time (sec)'].max()} seconds")
