from main import conversation_flow, appointments

def test_conversation():
    """
    Test script to simulate conversations and validate results.
    """
    test_inputs = [
        "Hi, I would like to book an appointment.",  # Test 1: Greeting and appointment initiation
        "August 10th at 10 AM",                      # Test 2: Booking an appointment
        "Check previous appointments",              # Test 3: Check existing appointments
        "Bye"                                       # Test 4: Termination of conversation
    ]
    expected_responses = [
        "Sure, can you provide the date and time for the appointment?",  # Response to Test 1
        "Booking your appointment for August 10th at 10 AM... Done! Your appointment ID is 1.",  # Response to Test 2
        "Here are your previously booked appointments:\nID 1: August 10th at 10 AM",  # Response to Test 3
        "Goodbye! Take care and have a great day!"  # Response to Test 4
    ]

    print("Starting tests...\n")
    for i, user_input in enumerate(test_inputs):
        print(f"Test {i+1}:")
        response = conversation_flow(user_input)
        print(f"Patient: {user_input}")
        print(f"Agent: {response}")
        assert response == expected_responses[i], f"Test {i+1} failed! Expected: {expected_responses[i]}, Got: {response}"
        print("Test passed!\n")

    # Verify appointment storage
    print("Verifying appointments...\n")
    assert len(appointments) == 1, "Failed: Appointments count mismatch."
    assert appointments[1]["date"] == "August 10th", "Failed: Date mismatch."
    assert appointments[1]["time"] == "10 AM", "Failed: Time mismatch."
    print("All tests passed!")

if __name__ == "__main__":
    test_conversation()
