// This file is parsed by Python's str.format() function.
// For this reason, doubling curly braces is required to escape those that are not part of the formatting placeholders.
// The final output will contain single curly braces as intended in JavaScript code.

if (flvjs.isSupported()) {{
    var videoElement = document.getElementById('{element_id}');
    var flvPlayer = flvjs.createPlayer({{
        type: 'flv',
        url: '{base_url}live/livestream.flv'
    }});
    flvPlayer.attachMediaElement(videoElement);
    flvPlayer.load();
    flvPlayer.play();
}}
