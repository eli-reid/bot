class twitchErrors:
    class TwitchAuthorizationFailed(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)

    class TwitchRepsonseCRSFInvaid(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)