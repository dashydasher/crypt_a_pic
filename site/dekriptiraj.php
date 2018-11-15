<form id="dekriptiraj_form" action="" method="post" enctype="multipart/form-data">
    <input type="file" name="file" id="file" required >
    <button id="kriptiraj_btn" type="submit">Dekriptiraj</button>
</form>

<br>

<strong id="poruka" hidden></strong>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<script>
    $("#dekriptiraj_form").on('submit',(function(e) {
        e.preventDefault();
        $.ajax({
            url: "dekriptiraj-sliku.php",
            type: "POST",
            data: new FormData(this),
            contentType: false,
            cache: false,
            processData:false,
            success: function(data) {
                if (data.uspjeh == true) {
                    $("#poruka").text(data.poruka);
                    $("#poruka").show();
                } else {
                    console.log("pogreska: " + data.poruka);
                }
            }
        });
    }));

</script>
