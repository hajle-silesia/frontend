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
