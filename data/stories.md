## fallback
- utter_default

## greeting path 1
* greet
- utter_greet
* fine_normal
- utter_help
* news
- utter_ofc
- action_get_feed
* thanks
- utter_anything_else
* mood_deny
- utter_bye



## fine path 1
* fine_normal
- utter_help

## fine path 2
* fine_ask
- utter_reply

## feed path
* feed
- utter_ofc
- action_get_feed

## thanks path 1
* thanks
- utter_anything_else

## bye path 1
* bye
- utter_bye