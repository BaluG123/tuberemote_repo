var loop=document.querySelector('#loop')
function change() {
    var vid=document.querySelector('.detail-video')
    vid.loop=true;
    vid.load();
}
loop.addEventListener('click',change)
