from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import db_helper
import generic_helper

app = FastAPI()

inprogress_recommendations = {}

@app.post("/")
async def handle_request(request: Request):
    payload = await request.json()

    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
    session_id = generic_helper.extract_session_id(output_contexts[0]["name"])

    intent_handler_dict = {
        'recommend.movie': recommend_movie,
    }

    return intent_handler_dict[intent](parameters, session_id)

def save_recommendation_to_db(recommendation: str):
    # Replace this with your actual logic to save the recommendation to a database
    pass

def recommend_movie(parameters: dict, session_id: str):
    mood = parameters.get("mood")
    interest = parameters.get("interest")

    if mood:
        recommendation = get_recommendation_by_mood(mood)
    elif interest:
        recommendation = get_recommendation_by_interest(interest)
    else:
        recommendation = "Sorry, I couldn't find a recommendation based on your input."

    if session_id in inprogress_recommendations:
        del inprogress_recommendations[session_id]

    save_recommendation_to_db(recommendation)

    return JSONResponse(content={
        "fulfillmentText": recommendation
    })

def get_recommendation_by_mood(mood: str):
    # Replace this with your actual logic to recommend movies based on mood
    if mood.lower() == "happy":
        return "You might enjoy watching 'La La Land'!"
    elif mood.lower() == "sad":
        return "How about watching 'The Pursuit of Happyness'?"
    else:
        return "Sorry, I couldn't find a recommendation based on your mood."

def get_recommendation_by_interest(interest: str):
    # Replace this with your actual logic to recommend movies based on interest
    if interest.lower() == "action":
        return "Check out 'The Dark Knight' for some action-packed entertainment!"
    elif interest.lower() == "comedy":
        return "Get ready to laugh with 'Superbad'!"
    else:
        return "Sorry, I couldn't find a recommendation based on your interest."
