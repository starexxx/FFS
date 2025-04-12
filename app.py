from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search_players():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Name parameter is required'}), 400
    
    try:
        # First API call to search for players
        search_url = f"https://ariflexlabs-search-api.vercel.app/search?name={name}"
        response = requests.get(search_url)
        response.raise_for_status()
        data = response.json()
        
        # Process the data to collect all players
        all_players = []
        for region_data in data:
            if region_data.get('result', {}).get('player'):
                all_players.extend(region_data['result']['player'])
        
        return jsonify(all_players)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/player_info')
def player_info():
    uid = request.args.get('uid')
    region = request.args.get('region')
    
    if not uid or not region:
        return jsonify({'error': 'UID and region parameters are required'}), 400
    
    try:
        # Second API call to get player details
        info_url = f"https://sigma-ff-info-api.vercel.app/player_info?uid={uid}&region={region}&key=SIGMAxBOY"
        response = requests.get(info_url)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
