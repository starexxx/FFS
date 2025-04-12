from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Fire Player Search</title>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        @font-face {
            font-family: 'GFF Latin';
            src: url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Thin.eot');
            src: local('GFF Latin Thin'), local('GFF-Latin-Thin'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Thin.eot?#iefix') format('embedded-opentype'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Thin.woff2') format('woff2'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Thin.woff') format('woff'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Thin.ttf') format('truetype');
            font-weight: 100;
            font-style: normal;
            font-display: swap;
        }

        @font-face {
            font-family: 'GFF Latin';
            src: url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Bold.eot');
            src: local('GFF Latin Bold'), local('GFF-Latin-Bold'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Bold.eot?#iefix') format('embedded-opentype'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Bold.woff2') format('woff2'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Bold.woff') format('woff'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Bold.ttf') format('truetype');
            font-weight: bold;
            font-style: normal;
            font-display: swap;
        }

        @font-face {
            font-family: 'GFF Latin';
            src: url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Regular.eot');
            src: local('GFF Latin Regular'), local('GFF-Latin-Regular'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Regular.eot?#iefix') format('embedded-opentype'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Regular.woff2') format('woff2'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Regular.woff') format('woff'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Regular.ttf') format('truetype');
            font-weight: normal;
            font-style: normal;
            font-display: swap;
        }

        @font-face {
            font-family: 'GFF Latin';
            src: url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Medium.eot');
            src: local('GFF Latin Medium'), local('GFF-Latin-Medium'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Medium.eot?#iefix') format('embedded-opentype'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Medium.woff2') format('woff2'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Medium.woff') format('woff'),
                url('https://raw.githubusercontent.com/starexxx/Fonts/main/GFF-Latin-Medium.ttf') format('truetype');
            font-weight: 500;
            font-style: normal;
            font-display: swap;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'GFF Latin', sans-serif;
        }
        
        body {
            background-color: #000;
            color: white;
            padding: 20px;
            background-image: url('https://raw.githubusercontent.com/starexxx/Fonts/main/36b630e138a0ad03d3c15c6c52d46044.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            min-height: 100vh;
            user-select: none;
            -webkit-tap-highlight-color: transparent;
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: transparent;
            padding: 20px;
        }
        
        header {
            text-align: left;
            margin-bottom: 30px;
        }
        
        h1 {
            color: #fff;
            margin-bottom: 10px;
            font-size: 28px;
            font-weight: 500;
        }
        
        .search-container {
            position: relative;
            margin-bottom: 30px;
        }
        
        #playerName {
            width: 100%;
            padding: 12px 50px 12px 15px;
            border-bottom: 1px solid #fff;
            border-top: none;
            outline: none;
            border-left: none;
            border-right: none;
            border-radius: 0px;
            background-color: transparent;
            color: #91a6bf;
            font-size: 16px;
        }
        #playerName::placeholder {color: #91a6bf;}
        #searchBtn {
            position: absolute;
            right: 10px;
            top: 50%;
            transform: translateY(-50%);
            background: url('https://raw.githubusercontent.com/starexxx/Fonts/main/download.svg') no-repeat center;
            background-size: contain;
            width: 20px;
            height: 20px;
            border: none;
            cursor: pointer;
        }
        
        .results-container {
            display: none;
        }
        
        .players-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
            gap: 10px;
            padding: 15px 0;
        }
        
        .player-card {
            background-color: rgba(0, 0, 0, 0.5);
            padding: 15px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .player-card:hover {
            transform: translateY(-3px);
        }
        
        .player-name {
            font-weight: bold;
            color: #fff;
            margin-bottom: 8px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            font-size: 16px;
        }
        
        .player-info {
            font-size: 14px;
            color: #aaa;
            margin-bottom: 5px;
        }
        
        .player-details {
            display: none;
            margin-top: 15px;
            padding-top: 15px;
            border-top: 1px solid #aaa;
        }
        
        .player-card.expanded .player-details {
            display: block;
        }
        
        .detail-row {
            display: flex;
            margin-bottom: 8px;
        }
        
        .detail-label {
            font-weight: bold;
            color: #fff;
            width: 140px;
            flex-shrink: 0;
        }
        
        .detail-value {
            flex: 1;
            color: #ddd;
            word-break: break-word;
        }
        
        .loading {
            display: none;
            text-align: center;
            color: white;
            margin: 20px 0;
        }
        
        .error-message {
            color: #ff6b6b;
            text-align: center;
            margin: 20px 0;
            display: none;
            font-weight: bold;
        }
        
        .no-results {
            text-align: center;
            color: #91a6bf;
            padding: 20px;
            display: none;
            font-size: 18px;
        }
        
        footer {
            text-align: center;
            margin-top: 40px;
            color: #91a6bf;
            font-size: 14px;
        }
        
        .view-info-link {
            color: #4dabf7;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            margin-top: 10px;
        }
        
        .view-info-link:hover {
            text-decoration: underline;
        }
        
        @media (max-width: 600px) {
            .players-grid {
                grid-template-columns: 1fr;
            }
            
            h1 {
                font-size: 24px;
            }
            
            .detail-label {
                width: 120px;
                font-size: 14px;
            }
            
            .detail-value {
                font-size: 14px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>ACCOUNT CHECK</h1>
            <p style="color: #91a6bf;">Search players by nickname across all regions</p>
        </header>
        
        <div class="search-container">
            <input type="text" id="playerName" placeholder="ENTER NICKNAME" autocomplete="off">
            <button id="searchBtn"></button>
        </div>
        
        <div class="loading">
            <p>Searching for players...</p>
        </div>
        
        <div class="error-message">
            An error occurred. Please try again later.
        </div>
        
        <div class="no-results">
            No players found with that name. Try a different search term.
        </div>
        
        <div class="results-container">
            <div class="players-grid"></div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const playerNameInput = document.getElementById('playerName');
            const searchBtn = document.getElementById('searchBtn');
            const resultsContainer = document.querySelector('.results-container');
            const playersGrid = document.querySelector('.players-grid');
            const loadingElement = document.querySelector('.loading');
            const errorElement = document.querySelector('.error-message');
            const noResultsElement = document.querySelector('.no-results');
            
            searchBtn.addEventListener('click', searchPlayers);
            
            playerNameInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    searchPlayers();
                }
            });
            
            function searchPlayers() {
                const name = playerNameInput.value.trim();
                
                if (name === '') {
                    return;
                }
                
                loadingElement.style.display = 'block';
                errorElement.style.display = 'none';
                noResultsElement.style.display = 'none';
                resultsContainer.style.display = 'none';
                playersGrid.innerHTML = '';
                
                fetch(`/search?name=${encodeURIComponent(name)}`)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        return response.json();
                    })
                    .then(players => {
                        loadingElement.style.display = 'none';
                        
                        if (players.error) {
                            throw new Error(players.error);
                        }
                        
                        if (players.length === 0) {
                            noResultsElement.style.display = 'block';
                            return;
                        }
                        
                        displayResults(players);
                        resultsContainer.style.display = 'block';
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        loadingElement.style.display = 'none';
                        errorElement.textContent = error.message || 'An error occurred. Please try again later.';
                        errorElement.style.display = 'block';
                    });
            }
            
            function displayResults(players) {
                playersGrid.innerHTML = '';
                
                players.forEach(player => {
                    const playerCard = document.createElement('div');
                    playerCard.className = 'player-card';
                    playerCard.dataset.uid = player.accountId;
                    playerCard.dataset.region = player.region;
                    
                    playerCard.innerHTML = `
                        <div class="player-name">${player.nickname}</div>
                        <div class="player-info">Level: ${player.level}</div>
                        <div class="player-info">Region: ${player.region}</div>
                        <div class="player-info">UID: ${player.accountId}</div>
                        <div class="player-details"></div>
                    `;
                    
                    playerCard.addEventListener('click', function() {
                        const isExpanded = this.classList.contains('expanded');
                        document.querySelectorAll('.player-card').forEach(card => {
                            card.classList.remove('expanded');
                        });
                        if (!isExpanded) {
                            this.classList.add('expanded');
                            loadPlayerDetails(this, player);
                        }
                    });
                    
                    playersGrid.appendChild(playerCard);
                });
            }
            
            function loadPlayerDetails(cardElement, player) {
                const detailsContainer = cardElement.querySelector('.player-details');
                
                const apiUrl = `/player_info?uid=${player.accountId}&region=${player.region}`;
                
                detailsContainer.innerHTML = `
                    <div class="detail-row">
                        <div class="detail-label"></div>
                        <div class="detail-value">
                            <a href="https://sigma-ff-info-api.vercel.app/player_info?uid=${player.accountId}&region=${player.region}&key=SIGMAxBOY" class="view-info-link" target="_blank">View Details</a>
                        </div>
                    </div>
                `;
            }
        });
    </script>
</body>
</html>
    '''

@app.route('/search')
def search_players():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Name parameter is required'}), 400
    
    try:
        search_url = f"https://ariflexlabs-search-api.vercel.app/search?name={name}"
        response = requests.get(search_url)
        response.raise_for_status()
        data = response.json()

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
        info_url = f"https://sigma-ff-info-api.vercel.app/player_info?uid={uid}&region={region}&key=SIGMAxBOY"
        response = requests.get(info_url)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
