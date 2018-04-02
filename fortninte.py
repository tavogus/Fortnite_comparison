import requests
from flask import Flask,render_template,request

platform = 'pc'

URL = 'https://api.fortnitetracker.com/v1/profile/' + platform + '/{}' 

headers = {'TRN-Api-Key' : '3fccdb07-5060-4fde-a4e7-661ea0354663'}

app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
def index():
    player_one = None
    player_two = None
    player_one_stats = {}
    player_two_stats = {}

    if request.method == 'POST':
        player_one = request.form.get('playerOneName')

        if player_one:
            player_two = request.form.get('playerName')
        else:
            player_one = request.form.get('playerName')    

        player_one_result = requests.get(URL.format(player_one), headers=headers).json()['lifeTimeStats']
        player_one_stats = player_data(player_one_result)

        if player_two:
            player_two_result = requests.get(URL.format(player_two), headers=headers).json()['lifeTimeStats']
            player_two_stats = player_data(player_two_result)
            
            

    return render_template('index.html', player_one=player_one, player_two=player_two,
                                         player_one_stats=player_one_stats, player_two_stats=player_two_stats)
    

def player_data(api_data):
    
    temp_dict = {}

    for r in api_data:
        if r['key'] == 'Wins':
           temp_dict['wins'] = r['value']  
        if r['key'] == 'Kills':  
           temp_dict['kills'] = r['value']
        if r['key'] == 'Matches Played':  
           temp_dict['matches'] = r['value']  

    return temp_dict

if __name__ == '__main__':
    app.run(debug=True)