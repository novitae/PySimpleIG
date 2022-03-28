from random import choice

URL = "https://www.instagram.com/"
BROWSER_UA = choice([
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-ch) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; ar) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Android 2.2; Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-HK) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; tr-TR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; nb-NO) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-cn) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5"
])
IOS_UA = choice([
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 211.0.0.21.118 (iPhone12,8; iOS 14_8; en_CL; en-CL; scale=2.00; 750x1334; 327311214)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 210.0.0.16.67 (iPhone11,8; iOS 15_0_1; es_CL; es-CL; scale=2.00; 828x1792; 325544617)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 212.1.0.25.118 (iPhone13,1; iOS 14_7_1; en_SA@calendar=gregorian; en-SA; scale=2.88; 1080x2338; 329643252) NW/3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 212.1.0.25.118 (iPhone13,1; iOS 14_7_1; en_SA@calendar=gregorian; en-SA; scale=2.88; 1080x2338; 329643252)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 213.0.0.19.117 (iPhone14,2; iOS 15_1; da_DK; da-DK; scale=3.00; 1170x2532; 330663239)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 213.0.0.19.117 (iPhone12,1; iOS 14_8; pt_BR; pt-BR; scale=2.00; 828x1792; 330663239)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 212.1.0.25.118 (iPhone12,3; iOS 14_7_1; ru_RU; ru-RU; scale=3.00; 1125x2436; 329643252) NW/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 213.0.0.19.117 (iPhone13,4; iOS 15_1; it_IT; it; scale=3.00; 1284x2778; 330663239) NW/3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 213.0.0.19.117 (iPhone13,1; iOS 15_0_2; ru_RU; ru; scale=2.88; 1080x2338; 330663239)",
    "Mozilla/5.0 (iPad; CPU OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 213.0.0.19.117 (iPad8,9; iPadOS 15_1; en_IT; en-GB; scale=2.00; 750x1334; 330663239)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 208.0.0.26.131 (iPhone12,3; iOS 13_5_1; ru_RU; ru-RU; scale=3.00; 1125x2436; 322184766) NW/3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 208.0.0.26.131 (iPhone12,3; iOS 13_5_1; ru_RU; ru-RU; scale=3.00; 1125x2436; 322184766)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 213.0.0.19.117 (iPhone13,3; iOS 14_8_1; ru_RU; ru-RU; scale=3.00; 1170x2532; 330663239) NW/3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 213.0.0.19.117 (iPhone13,3; iOS 14_8_1; ru_RU; ru-RU; scale=3.00; 1170x2532; 330663239)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 213.0.0.19.117 (iPhone13,2; iOS 15_0; ru_RU; ru-RU; scale=3.00; 1170x2532; 330663239) NW/1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 213.0.0.19.117 (iPhone9,1; iOS 14_8_1; it_IT; it-IT; scale=2.00; 750x1334; 330663239)",
])

DEFAULT_HEADERS = {"User-Agent": BROWSER_UA}

self_infos_endpoints = {
    "access_tool": "accounts/access_tool/?__a=1",
    "account_privacy_changes": "accounts/access_tool/account_privacy_changes?__a=1",
    "accounts_following_you": "accounts/access_tool/accounts_following_you?__a=1",
    "accounts_you_blocked": "accounts/access_tool/accounts_you_blocked?__a=1",
    "accounts_you_follow": "accounts/access_tool/accounts_you_follow?__a=1",
    "accounts_you_hide_stories_from": "accounts/access_tool/accounts_you_hide_stories_from?__a=1",
    "ads_interests": "accounts/access_tool/ads_interests?__a=1",
    "current_follow_requests": "accounts/access_tool/current_follow_requests?__a=1",
    "emails_sent": "emails/emails_sent/?__a=1",
    "former_bio_texts": "accounts/access_tool/former_bio_texts?__a=1",
    "former_emails": "accounts/access_tool/former_emails?__a=1",
    "former_full_names": "accounts/access_tool/former_full_names?__a=1",
    "former_links_in_bio": "accounts/access_tool/former_links_in_bio?__a=1",
    "former_phones": "accounts/access_tool/former_phones?__a=1",
    "former_usernames": "accounts/access_tool/former_usernames?__a=1",
    "hashtags_you_follow": "accounts/access_tool/hashtags_you_follow?__a=1",
    "login_activity": "session/login_activity/?__a=1",
    "logouts": "accounts/access_tool/logouts?__a=1",
    "password_changes": "accounts/access_tool/password_changes?__a=1",
    "privacy_and_security": "accounts/privacy_and_security/?__a=1",
    "search_history": "accounts/access_tool/search_history?__a=1",
    "story_bookmarked_music": "accounts/access_tool/story_bookmarked_music?__a=1",
    "story_countdown_follows": "accounts/access_tool/story_countdown_follows?__a=1",
    "story_emoji_slider_votes": "accounts/access_tool/story_emoji_slider_votes?__a=1",
    "story_poll_votes": "accounts/access_tool/story_poll_votes?__a=1",
    "story_question_responses": "accounts/access_tool/story_question_responses?__a=1",
    "story_question_music_responses": "accounts/access_tool/story_question_music_responses?__a=1",
    "story_quiz_responses": "accounts/access_tool/story_quiz_responses?__a=1"
}