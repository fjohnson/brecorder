function add_row(row_class, row_html, row_header_id){
    var rows = $(row_class)
    var row = $(row_html)

    row.find(".row-remove").on("click", function(e, event){
        row.remove()
    })

    if(rows.length){
        row.insertAfter(rows[rows.length-1])
    }else{
        row.insertAfter(row_header_id)
    }
}

$("#addhop").on("click", function(event){
    add_row(".hops",
            '<div class="data row hops">\
                 <div class="col-md-3"><input type="text" class="form-control" name="hop" value=""></div>\
                 <div class="col-md-3"><input type="text" class="form-control" name="hop" value=""></div>\
                 <div class="col-md-3"><input type="text" class="form-control" name="hop" value=""></div>\
                 <div class="col-md-3 non_editable_column">\
                     <select form="save_form" name="hop">\
                         <option value="Boil" selected>Boil</option>\
                         <option value="Dryhop">Dryhop</option>\
                         <option value="FWH">FWH</option>\
                         <option value="Flame Out">Flame Out</option>\
                     </select>\
                     <button type="button" class="btn btn-default btn-xs">\
                       <span class="glyphicon glyphicon-minus row-remove" aria-hidden="true"></span>\
                     </button>\
                 </div>\
             </div>',
             "#hops_header")
})

$("#addoingredient").on("click", function(event){
    add_row(".oingredients",
            '<div class="data row oingredients">\
                <div class="col-md-4"><input type="text" class="form-control" name="oingredient" value=""></div>\
                <div class="col-md-4"><input type="text" class="form-control" name="oingredient" value=""></div>\
                <div class="col-md-4 form-inline">\
                  <input type="text" class="form-control" name="oingredient" value="">\
                  <button type="button" class="btn btn-default btn-xs">\
                      <span class="glyphicon glyphicon-minus row-remove" aria-hidden="true"></span>\
                  </button>\
                </div>\
            </div>',
            "#oingredients_header")
})

$("#addnote").on("click", function(event){
    add_row(".notes",
            '<div class="data row notes">\
                <div class="col-md-8"><textarea name="notes" rows="5" class="form-control"></textarea></div>\
                <div class="col-md-4 form-inline ">\
                    <input class="form-control" type="text" name="notes" value="">\
                    <button type="button" class="btn btn-default btn-xs">\
                        <span class="glyphicon glyphicon-minus row-remove" aria-hidden="true"></span>\
                    </button>\
              </div>\
            </div>',
            "#notes_header"
    )
})

$("#addfermentable").on("click", function(event){
    add_row(".fermentables",
            '<div class="data row fermentables">\
                <div class="col-md-4"><input type="text" class="form-control" name="fermentable" value=""></div>\
                <div class="col-md-2"><input type="text" class="form-control" name="fermentable" value=""></div>\
                <div class="col-md-2 non_editable_column"></div>\
                <div class="col-md-4 form-inline">\
                      <input type="text" class="form-control" name="fermentable" value="">\
                      <button type="button" class="btn btn-default btn-xs">\
                      <span class="glyphicon glyphicon-minus row-remove" aria-hidden="true"></span>\
                      </button>\
                </div>\
            </div>',
            "#fermentable_header")
})

$(".row-remove").on("click", function(e, event){
    var ancestors = $(this).parentsUntil('[class*="row"]')
    $(ancestors[ancestors.length-1]).parent().remove()
})

$("#save_link").on("click", function(event){
    event.preventDefault()
    $("#save_form").submit()
});

$("#fileSelect").on("click", function(event){
    $("#fileElem").click()
})

$(".img-remove").on("click", function(event){
    var ancestors = $(this).parentsUntil('[class="col-md-2"]')
    $(ancestors[ancestors.length-1]).parent().remove()
})

function add_image(path){

    var new_image = $('<div class="col-md-2">\
                          <div class="thumbnail">\
                              <a href="{}">\
                                  <img src="{}">\
                              </a>\
                              <div class="caption">\
                                  <p>Type here...</p>\
                              </div>\
                              <div class="col-md-2 buttongroup">\
                                  <button type="button" class="btn btn-default btn-xs">\
                                      <span class="glyphicon glyphicon-minus img-remove" aria-hidden="true"></span>\
                                  </button>\
                              </div>\
                          </div>\
                      </div>'.replace(/{}/g,path))

    new_image.find(".img-remove").on("click", function(event){
        new_image.remove()
    })

    $(".images").append(new_image)
}

function file_upload(file) {
  var xhr = new XMLHttpRequest();
  var formData = new FormData();
  formData.append("file", file, file.name)

  xhr.upload.addEventListener("error", function(e){
    alert("An error occurrred while transferring the file.")
  })

  xhr.upload.addEventListener("abort", function(e){
    alert("Transfer aborted.")
  })

  //Transfer completed without error event
  xhr.addEventListener("load", function(e){
        console.log(xhr.response)
        console.log(xhr.responseType)
        console.log(xhr.status)
        console.log(xhr.statusText)
        console.log(xhr.getAllResponseHeaders())
        add_image(xhr.response)
      }, false);


  xhr.open("POST", "/upload");
  xhr.send(formData)

}
