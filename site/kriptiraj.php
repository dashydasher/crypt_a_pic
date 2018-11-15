<form id="kriptiraj_form" action="" method="post" enctype="multipart/form-data">
    <input type="file" name="file" id="file" required>
    <input type="text" id="poruka" name="poruka" required placeholder="Kriptirana poruka" size="100">
    <button id="kriptiraj_btn" type="submit">Kriptiraj</button>
</form>

<a hidden id="image-link" download title="Download">
    <img id="image">
</a>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<script>
    $('#kriptiraj_form').submit(function () {
        event.preventDefault();
        var inputs = $('#kriptiraj_form :input');
        var serializedData = inputs.serialize();

        inputs.prop("disabled", true);



        var $formdata = new FormData($(this)[0]);
        $formdata.append('poruka', $('#poruka').val());
        $formdata.append("file", document.getElementById('file').files[0]);
        $.ajax({
            url: "kriptiraj-sliku.php",
            type: "POST",
            data: $formdata,
            contentType: false,
            cache: false,
            processData:false,
            success: function(data) {
                console.log("success: " + data);
                $('#image').attr("src", "encrypt_in_decrypted.ppm");
                $('#image-link').attr("href", "encrypt_in_decrypted.ppm");
                $('#image-link').show();
                $("image-link").trigger("click");
            },
            error: function(jqXHR, textStatus, errorThrown){
                console.log("error: " + errorThrown);
            }
        });
        inputs.prop("disabled", false);

        /*
        $.post("kriptiraj-sliku.php", serializedData)
            .done(function(data) {


                //tu izmjeni putanju do novokreirane slike

                $('#image').attr("src", "test.png");
                $('#image-link').attr("href", "test.png");
                $('#image-link').show();
            })
            .fail(function(xhr) {
                console.log(xhr.status + ": " + "Nije dobro!");
            })
            .always(function() {
                inputs.prop("disabled", false);
            });
            */
        });
</script>
