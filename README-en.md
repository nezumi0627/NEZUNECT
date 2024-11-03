# NEZUNECT🍪

NEZUNECT is an unofficial API wrapper for the social networking platform [Subnect](https://subnect.com/).

This library provides an easy-to-use interface for Cookie🍪 interacting with Subnect's features.

[日本語](README.md)

## Features

- Get profile information
- Create and search posts
- Like and follow functions
- Update profile
- Get top posts
- Get sessions
- Get notifications
- Change notification sound
- Get bookmarks
- Add bookmarks
- Change theme
- Change language
- Change notification settings
- Change email address
- Change username

## Installation

NEZUNECT can be installed using the following git command:

```
git clone https://github.com/nezumi0627/NEZUNECT.git
```

## Usage

Here is an example of how to use NEZUNECT:

```python
from nezunect import NEZUNECT

# Initialize the NEZUNECT client
bot = NEZUNECT(cookie="your_cookie_here", debug=True)
bot.initialize()

# Retrieve profile information
profile = bot.get_profile("username")
print(f"Nickname: {profile['nickname']}")

# Create a post
post_result = bot.create_post("Hello Nezunect-Unofficial-API!")
print(f"Post created. Post ID: {post_result['postId']}")

# Close the session
bot.close()
```

For more detailed usage, please refer to the documentation.

## Contributing

Contributions are welcome! Feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This is an unofficial API wrapper and is not affiliated with or endorsed by Subnect. Use at your own risk.
