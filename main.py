from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain


# Initialize LangChain
chat_model = ChatOpenAI(temperature=0.7, openai_api_key="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")
prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="You are a friendly assistant at a dental clinic. {history} Patient: {input}"
)
conversation_chain = ConversationChain(llm=chat_model, prompt=prompt)

# Simulated storage for appointments
appointments = {}

def book_appointment(date, time):
    appointment_id = len(appointments) + 1
    appointments[appointment_id] = {"date": date, "time": time}
    return appointment_id

def check_appointments():
    """
    List all previously booked appointments.
    """
    if not appointments:
        return "You don't have any booked appointments yet."
    
    response = "Here are your previously booked appointments:\n"
    for appointment_id, details in appointments.items():
        response += f"ID {appointment_id}: {details['date']} at {details['time']}\n"
    return response.strip()

def conversation_flow(user_input):
    """
    Basic conversation flow logic for booking appointments with greetings and termination handling.
    """
    if user_input.lower() in ["hi", "hello"]:
        return "Hello! Welcome to the Dental Clinic Assistant. How can I help you today?"
    elif user_input.lower() in ["bye", "goodbye"]:
        return "Goodbye! Take care and have a great day!"
    elif "check previous appointments" in user_input.lower():
        return check_appointments()
    elif "book an appointment" in user_input.lower():
        return "Sure, can you provide the date and time for the appointment?"
    elif "at" in user_input:  # Example parsing for 'Date at Time'
        try:
            # Preserve original case for date and time
            date, time = user_input.split(" at ")
            date, time = date.strip(), time.strip()
            appointment_id = book_appointment(date, time)
            return f"Booking your appointment for {date} at {time}... Done! Your appointment ID is {appointment_id}."
        except ValueError:
            return "Please provide the date and time in the format 'Date at Time'."
    else:
        return "I didn't understand that. Could you please provide more details?"

if __name__ == "__main__":
    print("Welcome to the Dental Clinic Assistant!")
    print("Type 'bye' or 'goodbye' to end the conversation.\n")
    history = ""
    while True:
        user_input = input("Patient: ")
        response = conversation_flow(user_input)
        print(f"Agent: {response}")
        
        if user_input.lower() in ["bye", "goodbye"]:
            break
        
        history += f"Patient: {user_input}\nAgent: {response}\n"
