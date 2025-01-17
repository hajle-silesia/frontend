if (flvjs.isSupported()) {
    var videoElement = document.getElementById('mlt_sightglass_video');
    var flvPlayer = flvjs.createPlayer({
        type: 'flv',
        url: 'http://srs-server.default.svc.cluster.local:8080/live/livestream.flv'
    });
    flvPlayer.attachMediaElement(videoElement);
    flvPlayer.load();
    flvPlayer.play();
}
