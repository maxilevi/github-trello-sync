import json
from trello import TrelloClient
from github import Github

def select_board(client, board_name):
    all_boards = client.list_boards()
    for board in all_boards:
        print(f"Found board '{board.name}'")
        if board_name == board.name:
            return board
    raise ValueError(f'Failed to find board {board_name}')

def assert_valid_config(config: dict):
    if 'repo_name' not in config or 'github_access_token' not in config or 'board_name' not in config or 'trello_api_key' not in config:
        raise ValueError(f'Invalid config.')


with open('./config.json', 'r') as fp:
    config = json.load(fp)

client = TrelloClient(
    api_key=config['trello_api_key'],
    api_secret=config['trello_api_secret'],
    token=config['trello_token']
)
github = Github(config['github_access_token'])

board = select_board(client, config['board_name'])
for card in board.all_cards():
    card.delete()

for t_list in board.all_lists():
    t_list.close()

repo = github.get_repo(config['repo_name'])
open_milestones = repo.get_milestones(state='open')
open_issues = repo.get_issues(state='open')
added_issues = []

for milestone in open_milestones:
    trello_list = board.add_list(milestone.title)
    print(f'Creating list {milestone.title}')
    for issue in open_issues:
        if issue.milestone is not None and issue.milestone.title == milestone.title:
            print(f'Adding card {issue.title} to "{milestone.title}"')
            added_issues.append(issue.title)
            trello_list.add_card(issue.title)

open_issues_list = board.add_list('Open Issues')
for issue in open_issues:
    if issue.title not in added_issues:
        open_issues_list.add_card(issue.title)
        print(f'Adding card {issue.title} to Open Issues')



