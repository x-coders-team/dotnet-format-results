from services.ServiceAbstract import ServiceAbstract
from githubkit import GitHub, ActionAuthStrategy, Response
from pprint import pprint
from inspect import getmembers

class GitHubChecksService(ServiceAbstract):
    _github = None
    _gitHubConfig = None
    _checkName = ".NET Format Results [beta]"
    _externalId = "action-dotnet-format-results"
    _debug = False

    def __init__(self, di = None, app = None):
        """_summary_

        Args:
            di (DepedencyInjection, optional): _description_. Defaults to None.
        """

        super().__init__(di, app)
        self._github = GitHub(ActionAuthStrategy())
        self._gitHubConfig = self.injectConfigByName('github_config')
        self._debug = self.injectConfigByName('debug')

    async def createNewCheck(self):
        repositoryMetadata = self._getRepositoryName(self._gitHubConfig['REPOSITORY'])

        resp = await self._github.rest.checks.async_create(
            head_sha = self._gitHubConfig['SHA'],
            owner = repositoryMetadata['owner'],
            repo = repositoryMetadata['repository'],
            name = self._checkName,
            status = 'completed',
            conclusion = 'success',
            output = {
                "title": self._checkName,
                "summary": "summary OK",
                "text": "text OK"
            }
        )

        if self._debug:
            pprint(resp)

        pass

    def _getRepositoryName(self, ownerAndRepositorySetting):
        splitData = ownerAndRepositorySetting.split('/')

        return {
            "owner": splitData[0], 
            "repository": splitData[1], 
            "full": ownerAndRepositorySetting
        }
    