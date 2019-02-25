# github-trello-sync

Sync your github issues and milestones with a specified trello board

Example `config.json`
```json
{
  "github_access_token": "YOUR_GITHUB_ACCESS_TOKEN",
  "trello_api_key": "YOUR_TRELLO_API_KEY",
  "trello_api_secret": "YOUR_TRELLO_API_SECRET",
  "trello_token": "YOUR_TRELLO_TOKEN",
  "repo_name": "Zaphyk/github-trello-sync",
  "board_name": "NAME_OF_THE_TRELLO_BOARD"
}
```
After setting up the `config.json` just run the `sync.py` script and watch your trello board get synced!
