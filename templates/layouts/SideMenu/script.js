document.addEventListener('DOMContentLoaded', function() {
    const div = document.getElementById('layouts_sideMenu_div');
    
    div.addEventListener('mousedown', function(e) {
        let startX = e.clientX;
        let startWidth = this.offsetWidth;
        
        
        document.addEventListener('mousemove', onMouseMove);
        document.addEventListener('mouseup', onMouseUp);
    });

    function onMouseMove(e) {
        let newWidth = startWidth + (e.clientX - startX);
        div.style.width = `${newWidth}px`;
    }

    function onMouseUp() {
        document.removeEventListener('mousemove', onMouseMove);
        document.removeEventListener('mouseup', onMouseUp);
    }
});