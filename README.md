<h1 align="center">Spotify Status (README)</h1>
<p align="center">View what you listen at spotify.</p>

<p align="center">
   <a href="https://github.com/sndrjhlncgr/README-Spotify-Status/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/sndrjhlncgr/README-Spotify-Status"></a>
   <a href="https://github.com/sndrjhlncgr/README-Spotify-Status/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/sndrjhlncgr/README-Spotify-Status"></a>
   <a href="https://github.com/sndrjhlncgr/README-Spotify-Status/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/sndrjhlncgr/README-Spotify-Status"></a>
   <a href="https://github.com/sndrjhlncgr/README-Spotify-Status/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/sndrjhlncgr/README-Spotify-Status"></a>
<p align="center">

![Image of Sandro Cagara](https://i.ibb.co/Tmjxnhs/README-Spotify-Status-v2.jpg)
<p align="center">
   <h3>Demo</h3>
   <img src="https://readme-spotify-status-rho.vercel.app/api/run-spotify-status.py" alt="s4nx Playing Now" width="500" />
<p align="center">

Spotify for Developers
-----

* Create a [Spotify for Developers](https://developer.spotify.com/dashboard/applications) account
* Get Credentials
    * `Client ID`
    * `Client Secret`
* Go to **Edit Settings**
* Find **Redirect URIs**:
    * Add `http://localhost/callback/`

Get the Refresh Token from Spotify
-----

* Navigate to the following URL:
  <br/>
  **Note**: copy your Client ID and paste in **{SPOTIFY_CLIENT_ID}** below.

```
https://accounts.spotify.com/authorize?client_id={PUT_YOUR_SPOTIFY_CLIENT_ID_HERE}&response_type=code&scope=user-read-currently-playing,user-read-recently-played&redirect_uri=http://localhost/callback/
```

* After logging in, get the {GET_THE_TOKEN} portion of: `http://localhost/callback/?code={GET_THE_TOKEN}`

* Create a string combining `{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}` (e.g. `5n7o4v5a3t7o5r2e3m1:5a8n7d3r4e2w5n8o2v3a7c5`) and encode into [Base64](https://www.base64encode.org/).

* Then run a [curl command](https://reqbin.com/curl):
```sh
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: Basic {YOUR_BASE64}" -d "grant_type=authorization_code&redirect_uri=http://localhost/callback/&code={YOUR_TOKEN}" https://accounts.spotify.com/api/token
```

* Then save the Refresh token

Configure Vercel Application
------
* Fork this [Spotify Status](https://github.com/sndrjhlncgr/Spotify-Status)

* Register on [Vercel](https://vercel.com/)

* Create project linked to your forked respository
  
  ![Vercel](https://i.ibb.co/sHhywHD/dasddas.jpg)

* Add Project Name and Environment Variables:
   Warning: Avoid white spaces!!
  - `SPOTIFY_REFRESH_TOKEN`
  - `SPOTIFY_CLIENT_ID`
  - `SPOTIFY_SECRET`
  - `SPOTIFY_BAR_COLOR` 
     - `Hex Color`
  - `SPOTIFY_BADGE_COLOR`
    - `Hex Color`
        
  ![Vercel](https://i.ibb.co/vv5z4yP/Untitled.png)
  
 * Deploy

Put this in your README.md
------
<h3>Small</h3>

<img src="https://readme-spotify-status-rho.vercel.app/api/run-spotify-status.py" alt="s4nx Playing Now" width="350" />

``` 
[<img src="https://{DOMAIN_OF_YOUR_VERCEL_APP}/api/run-spotify-status" alt="Your alt what" width="350" />](LINK_TO_YOUR_ACCOUNT)
```

<h3>Medium</h3>

<img src="https://readme-spotify-status-rho.vercel.app/api/run-spotify-status.py" alt="s4nx Playing Now" width="400" />

``` 
[<img src="https://{DOMAIN_OF_YOUR_VERCEL_APP}/api/run-spotify-status" alt="Your alt what" width="400" />](LINK_TO_YOUR_ACCOUNT)
```

<h3>Large</h3>

<img src="https://readme-spotify-status-rho.vercel.app/api/run-spotify-status.py" alt="s4nx Playing Now" width="500" />

``` 
[<img src="https://{DOMAIN_OF_YOUR_VERCEL_APP}/api/run-spotify-status" alt="Your alt what" width="500" />](LINK_TO_YOUR_ACCOUNT)
```

Contribution
------
Feel Free to contribute, PR are the most welcome :)

License
------
Copyright (c) 2020 Sandro Cagara | Spotify Status
