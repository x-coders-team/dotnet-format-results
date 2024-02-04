from services.ServiceAbstract import ServiceAbstract
from githubkit import GitHub, ActionAuthStrategy, Response

class GitHubChecksService(ServiceAbstract):
    _github = None
    _owner = "ACTION-DOTNET-FORMAT-RESULTS"
    _repo = "REPO"
    _checkName = ".NET Format Results [beta]"
    _externalId = "action-dotnet-format-results"

    def __init__(self, di = None):
        """_summary_

        Args:
            di (DepedencyInjection, optional): _description_. Defaults to None.
        """

        super().__init__(di)
        self._github = GitHub(ActionAuthStrategy())

    def CreateNewCheck(self):
        resp = self._github.rest.checks.async_create(
            owner = self._owner,
            repo = self._repo,
            name = self._checkName,
            external_id = self._externalId,
            status = 'completed',
            conclusion = 'skipped',
            output = {
                "title": ".NET Format Results [beta]",
                "summary": "",
                "text": "",
            }
        )
        pass
    