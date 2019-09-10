/* Any JavaScript here will be loaded for all users on every page load. */

/** Collapsible tables *********************************************************
 *
 *  Description: Allows tables to be collapsed, showing only the header.
 */

var autoCollapse = 2;
var collapseCaption = "hide";
var expandCaption = "show";

function collapseTable( tableIndex )
{
    var Button = document.getElementById( "collapseButton" + tableIndex );
    var Table = document.getElementById( "collapsibleTable" + tableIndex );

    if ( !Table || !Button ) {
        return false;
    }

    var Rows = Table.rows;

    if ( Button.firstChild.data == collapseCaption ) {
        for ( var i = 1; i < Rows.length; i++ ) {
            Rows[i].style.display = "none";
        }
        Button.firstChild.data = expandCaption;
    } else {
        for ( var i = 1; i < Rows.length; i++ ) {
            Rows[i].style.display = Rows[0].style.display;
        }
        Button.firstChild.data = collapseCaption;
    }
}

function createCollapseButtons()
{
    var tableIndex = 0;
    var NavigationBoxes = new Object();
    var Tables = document.getElementsByTagName( "table" );

    for ( var i = 0; i < Tables.length; i++ ) {
        if ( hasClass( Tables[i], "collapsible" ) ) {

            /* only add button and increment count if there is a header row to work with */
            var HeaderRow = Tables[i].getElementsByTagName( "tr" )[0];
            if (!HeaderRow) continue;
            var Header = HeaderRow.getElementsByTagName( "th" )[0];
            if (!Header) continue;

            NavigationBoxes[ tableIndex ] = Tables[i];
            Tables[i].setAttribute( "id", "collapsibleTable" + tableIndex );

            var Button     = document.createElement( "span" );
            var ButtonLink = document.createElement( "a" );
            var ButtonText = document.createTextNode( collapseCaption );

            Button.style.styleFloat = "right";
            Button.style.cssFloat = "right";
            Button.style.fontWeight = "normal";
            Button.style.textAlign = "right";
            Button.style.width = "6em";

            ButtonLink.style.color = Header.style.color;
            ButtonLink.setAttribute( "id", "collapseButton" + tableIndex );
            ButtonLink.setAttribute( "href", "javascript:collapseTable(" + tableIndex + ");" );
            ButtonLink.appendChild( ButtonText );

            Button.appendChild( document.createTextNode( "[" ) );
            Button.appendChild( ButtonLink );
            Button.appendChild( document.createTextNode( "]" ) );

            Header.insertBefore( Button, Header.childNodes[0] );
            tableIndex++;
        }
    }

    for ( var i = 0;  i < tableIndex; i++ ) {
        if ( hasClass( NavigationBoxes[i], "collapsed" ) || ( tableIndex >= autoCollapse && hasClass( NavigationBoxes[i], "autocollapse" ) ) ) {
            collapseTable( i );
        }
    }
}

addOnloadHook( createCollapseButtons );

// adds show/hide-button to navigation bars
 function createNavigationBarToggleButton()
 {
    var indexNavigationBar = 0;
    // iterate over all < div >-elements 
    var divs = document.getElementsByTagName("div");
    for(
            var i=0; 
            NavFrame = divs[i]; 
            i++
        ) {
        // if found a navigation bar
        if (hasClass(NavFrame, "NavFrame")) {

            indexNavigationBar++;
            var NavToggle = document.createElement("a");
            NavToggle.className = 'NavToggle';
            NavToggle.setAttribute('id', 'NavToggle' + indexNavigationBar);
            NavToggle.setAttribute('href', 'javascript:toggleNavigationBar(' + indexNavigationBar + ');');

            var NavToggleText = document.createTextNode(NavigationBarHide);
            for (
                 var NavChild = NavFrame.firstChild;
                 NavChild != null;
                 NavChild = NavChild.nextSibling
                ) {
                if ( hasClass( NavChild, 'NavPic' ) || hasClass( NavChild, 'NavContent' ) ) {
                    if (NavChild.style.display == 'none') {
                        NavToggleText = document.createTextNode(NavigationBarShow);
                        break;
                    }
                }
            }
        }
    }
}



/* Table Pagers */
$.fn.tablepager = function() {
    function the_pager() {
        var table = this;
        var tbody = table.tBodies[0];
        var $pager;
        var count;
        var pagesize;
        var numpages;
        var page;
        
        /* Get the table rows that are to be paged.
         * The class .tablepager-initallyhidden is added to rows during initialization. */
        function rows() {
            var $rows = $(tbody).find('tr:not(.tablepager-initiallyhidden)');
            return $rows;
        }

        /* Sets the visibility of rows.
         * Hidden rows will be hidden by adding the clas .tablepager-hide. */
        function set_visibility() {
            var $rows = rows();
            var min = (page - 1) * pagesize;
            var max = page * pagesize;
            $rows.each(function(idx) {
                if (idx >= min && idx < max)
                    $(this).removeClass('tablepager-hide');
                else
                    $(this).addClass('tablepager-hide');
            });
        }

        /* Jump to new page. */
        function set_page(newpage) {
            page = newpage;
            if (page < 1) page = 1;
            if (page > numpages) page = numpages;
            $pager.find('.tablepager-display').val(page + "/" + numpages);
            set_visibility();
        }
        
        /* Recalculate number of elements. */
        function set_elements() {
            count = rows().length;
            numpages = Math.ceil(count / pagesize) || 1;
            set_page(page); /* Recalculate page number limits and visibility. */
        }
        
        /* Sets page size. */
        function set_pagesize(newpagesize) {
            var currpos = ((page || 1) - 1) * (pagesize || 1);
            pagesize = newpagesize;
            numpages = Math.ceil(count / pagesize) || 1;
            set_page(Math.floor(currpos / pagesize) + 1); /* Try to jump to the page so the same elements are shown. */
        }
        
        /* Creates pager widget from HTML template, adds event handlers. */
        function create_pager() {
            var pagerhtml = 
                '<div class="tablepager-pager">'+
                '<button type="button" class="tablepager-first"></button>'+
                '<button type="button" class="tablepager-prev"></button>'+
                '<input type="text" class="tablepager-display" readonly>'+
                '<button type="button" class="tablepager-next"></button>'+
                '<button type="button" class="tablepager-last"></button>'+
                '<select class="tablepager-pagesize">'+
                '<option selected value="10">×10</option>'+
                '<option value="20">×20</option>'+
                '<option value="50">×50</option>'+
                '<option value="999999">All</option>'+
                '</select>'+
                '</div>';
            var templateid = $(table).attr('data-pager-template-id') || "";
            if (templateid != "")
                $pager = $($('#' + templateid).html());
            else
                $pager = $(pagerhtml);
            var containerid = $(table).attr('data-pager-id') || "";
            if (containerid != "")
                $pager.appendTo($('#' + containerid));
            else
                $pager.insertBefore(table);

            $pager.find('.tablepager-first').on('click', function() { set_page(1); });
            $pager.find('.tablepager-prev').on('click', function() { set_page(page - 1); });
            $pager.find('.tablepager-next').on('click', function() { set_page(page + 1); });
            $pager.find('.tablepager-last').on('click', function() { set_page(numpages); });
            $pager.find('.tablepager-pagesize').on('change', function() { set_pagesize(+this.value || 10); });
            $(table).on('tablesorter-sorted', set_visibility);
            $(table).on('tablepager-elements', set_elements);
        }
        
        /* Initializes pager. */
        function initialize_pager() {
            $(tbody).find('tr:not(:visible)').addClass('tablepager-initiallyhidden');
            count = rows().length;
            set_pagesize(+$pager.find('.tablepager-pagesize').val() || 10);
        }
        
        /* inicializálás */
        create_pager();
        initialize_pager();
    }
    
    return this.each(the_pager);
};