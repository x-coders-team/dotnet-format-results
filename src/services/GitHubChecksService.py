from services.ServiceAbstract import ServiceAbstract
from githubkit import GitHub, ActionAuthStrategy, Response
from pprint import pprint
from inspect import getmembers

class GitHubChecksService(ServiceAbstract):
    _github = None
    _gitHubConfig = None
    _checkName = ".NET Format Results [beta]"
    _externalId = "action-dotnet-format-results"

    def __init__(self, di = None, app = None):
        """_summary_

        Args:
            di (DepedencyInjection, optional): _description_. Defaults to None.
        """

        super().__init__(di, app)
        self._github = GitHub(ActionAuthStrategy())
        self._gitHubConfig = self.injectConfigByName('github_config')

    def CreateNewCheck(self):
        resp = self._github.rest.checks.async_create(
            head_sha = self._gitHubConfig['SHA'],
            owner = self._gitHubConfig['REPOSITORY_OWNER'],
            repo = self._gitHubConfig['REPOSITORY'],
            name = self._checkName,
            external_id = self._externalId,
            status = 'completed',
            conclusion = 'skipped'
        )

        pprint(resp)

        pass
    