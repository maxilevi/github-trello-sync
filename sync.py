import json
from trello import TrelloClient
from github import Github

def select_board(client, board_name):
    all_boards = client.list_boards()
    for board in all_boards:
        if board_name is board.name:
            return board
    raise Error(f'Failed to find board {board_name}')

def assert_valid_config(config: dict):
    if 'repo_name' is not in config or 'github_access_token' is not in config or 'board_name' is not in config or 'trello_api_key' is not in config:
        raise Error(f'')


with open('./config.json', 'r') as fp:
    config = json.loads(fp)

client = TrelloClient(
    api_key='your-key',
    api_secret='your-secret',
    token='your-oauth-token-key',
    token_secret='your-oauth-token-secret'
)
github = Github("github_access_token")

board = select_board(client, config['board_name'])
for card in board.all_cards():
    card.delete()

for t_list in board.all_lists():
    t_list.close()

repo = github.get_repo(config['repo_name'])
open_milestones = repo.get_milestones(state='open')
added_issues = []
for milestone in milestones:
    trello_list = board.add_list(milestone.title())
    for issue in milestone.open_issues():
        added_issues.append(issue.title())
        trello_list.add_card(issue.title())

open_issues_list = board.add_list('Open Issues')
for issue in repo.get_issues(state='open'):
    if issue.title() not in added_issues:
        open_issues_list.add_card(issue.title())

close_issues_list = board.add_list('Closed Issues')
for issue in repo.get_issues(state='closed'):
    if issue.title() not in added_issues:
        close_issues_list.add_card(issue.title())

