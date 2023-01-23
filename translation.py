from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START_MESSAGE = '''**Hello, {}
Hello Mr, I am @mr_rahul_tk, Bulk Link Converter owner. I Can Convert Links Directly From Your Mdiskshortx.in Account,
    
1. Go To 👉 https://mdiskshortx.in/member/tools/api  
2. Than Copy API Key
3. Than Type /api than give a single space and than paste your API Key (see example to understand more...)**

**/api(space)API Key 
(See Example.👇)
Example:** `/api de303d5270f481aec928f39883da7b7f9a8812ac `

**➕ Hit** 👉 /Features To Know More Features Of This Bot.
**💁‍♀️ Hit** 👉 /help To Get Help.
**➕ Hit** 👉 /channel Command To Get Help About Adding your channel to bot.
**➕ Hit** 👉 /footer To Get Help About Adding your Custom Footer to bot.

If You Want Any **Other Shortner** Link Converter Bot Instead Of mdskshortx than **contact** at 👉 @mr_rahul_tk (all **shortners** support available.)
'''

HELP_MESSAGE = '''**Hello, {}
Hello Mr, I am @mr_rahul_tk, Bulk Link Converter owner. I Can Convert Links Directly From Your Mdiskshortx.in Account,
    
1. Go To 👉 https://mdiskshortx.in/member/tools/api  
2. Than Copy API Key
3. Than Type /api than give a single space and than paste your API Key (see example to understand more...)**

**/api(space)API Key 
(See Example.👇)
Example:** `/api de303d5270f481aec928f39883da7b7f9a8812ac `

**➕ Hit** 👉 /Features To Know More Features Of This Bot.


If You Want Any **Other Shortner** Link Converter Bot Instead Of mdskshortx than **contact** at 👉 @mr_rahul_tk (all **shortners** support available.)
'''

ABOUT_TEXT = '''**Hey! My name is @ShortnerFlyBot. I am Shortener Fly Link Converter Bot.**

**⚡Features⚡**

• I can **Convert any** links or posts to your **mdiskshortx** link / post. (Button Links Posts, Hidden links/Hyperlinks All Are Supported)

• I Can **auto** add custom **footer text** to your every post. Hit 👉 /footer To know more...

• I Can **auto** add custom **Header text** to your every post. Hit 👉 /Header To know more...

• I Can **replace / remove** other's **channel links** with **your channel** link. Hit 👉 /channel To know More...

• I Can **Automatically Replace** Your ***Banner** Image To images in the post. Hit  👉/Banner To Know More... 

• **No** need to share **password or email** to convert links.**

 Anyone who want to use any **other shortner** instead of ShortnerFly than **contact** at 👉 @mr_rahul_tk (all **shortners support** available.)

**Click On Custom Alias To Create Custom Link**
'''

CUSTOM_ALIAS_MESSAGE = """For Custom Alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/mdiskshortx.in | mdiskshortx.in"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""

ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('Custom Alias', callback_data=f'alias_conf')
        
    ],


])

HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('More Features', callback_data=f'about_command')
        
    ],


])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Get Api', url=f'https://mdiskshortx.in/member/tools/api')
    ]
])



BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data=f'help_command')
    ],

])

USER_ABOUT_MESSAGE = """
- Website: [{base_site}](https://mdiskshortx.in/ref/rngharman)

- Site Link {base_site} Current Linked API: {shortener_api}

- Replace Channel Username: @{username}

- Header Text: 
{header_text}

- Footer Text: 
{footer_text}

- Banner Image: {banner_image}
"""


SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/set_api [api]`
            
Ex: `/api de303d5270f481aec928f39883da7b7f9a8812ac `

Get API From [{base_site}](https://mdiskshortx.in/ref/rngharman)

Current {base_site} API: `{shortener_api}`"""

HEADER_MESSAGE = """Reply to the Header Text You Want

This Text will be added to the top of every message caption or text

For adding line break use \n
To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """**Reply tothefooter text you want**

Hello Mr, I am mdiskshortx.in , Bulk Link Converter / Uploader Bot From Linked miskshortx.in Account,

🌟 Just Type👉 /footer footer-text

Example:
/footer ━━━━━━━━━━━━━━━━━
💁‍♀️How To Download👇
👉 https://
━━━━━━━━━━━━━━━━━
🔥𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥🔥
👉 https://t.me/Herrypotterallpartinhindi

🤘 Hit 👉 /features To Know More Features Of This Bot.

- Message @mr_rahul_tk For More Help"""


USERNAME_TEXT = """**Hello Harman, I am mdiskshortx.in, Bulk Link Converter Bot From Linked mdiskshortx.in Account,**

**🌟 Type** /channel (channel link or username)

**example:**
/channel @mr_rahul_tk
Or
/channel https://t.me/mdisk_shortx

**🤘 Hit** 👉 /features Hello who_am_i, I am Mdiskshortx.in , Bulk Link Converter Bot. I Can Convert Links Directly From Your Mdiskshortx.in Account,

⚡️ Features ⚡️
• I can Convert any links or posts to your Mdiskshortx / post. (Button Links Posts, Hidden links/Hyperlinks All Are Supported)

• If send me a post which has Mdiskshortx.in Links, texts & images... Than i wiil replace all Mdiskshortx.in Links with Conveted Links From Your Linked api Account Automatic And Send Back To You.

• I can Convert unlimited mdiskshortx.in links at once. (if you are sending a list of urls.)

• No need to share password or email to convert links.

• I Can replace/remove other's channel's links with your channel link. Hit 👉 /add_channel To know more...

• I Can auto add custom footer text to your every post. Hit 👉 /footer To know more...

Anyone who want to use any other shortner instead of Mdiskshortner than contact at 👉 @mr_rahul_tk(all shortners support avilable.)t.

**- Message @mr_rahul_tk For More Help -**"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://telegra.ph/file/5e96340a91470256b387a.jpg`"""


BANNED_USER_TXT = """
Usage: `/ban [User ID]`

Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
