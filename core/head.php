<?php

/**
 * Head tags handler for the ClearOS theme.
 *
 * @category  Theme
 * @package   ClearOS
 * @author    ClearFoundation <developer@clearfoundation.com>
 * @copyright 2011-2012 ClearFoundation
 * @license   http://www.gnu.org/copyleft/gpl.html GNU General Public License version 3 or later
 * @link      http://www.clearfoundation.com/docs/developer/theming/
 */

//////////////////////////////////////////////////////////////////////////////
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
///////////////////////////////////////////////////////////////////////////////

/**
 * Returns additional <head> data required for the theme.
 *
 * @param string $theme_path them path
 *
 * @return string HTML output
 */

function theme_page_head($theme_path)
{
	$basepath = preg_replace('/\/core\/.*/', '', realpath(__FILE__));

	if (file_exists("$basepath/css/theme-extras.css"))
		$theme_extras = "<link type='text/css' href='$theme_path/css/theme-extras.css' rel='stylesheet'>\n";
	else
		$theme_extras = "\n";

	if (file_exists("$basepath/images/favicon-orange.ico"))
		$color = "orange";
	else
		$color = "green";

    return "
<!-- Theme Favicon -->
<link href='$theme_path/images/favicon-$color.ico' rel='shortcut icon' >

<!-- Theme Style Sheets -->
<link type='text/css' href='$theme_path/css/jquery-ui-1.8.22.custom.css' rel='stylesheet'>
<link type='text/css' href='$theme_path/css/jquery.jqplot.min.css' rel='stylesheet'>
<link type='text/css' href='$theme_path/css/superfish.css' rel='stylesheet'>
<link type='text/css' href='$theme_path/css/jquery.lightbox-0.5.css' rel='stylesheet'>
<link type='text/css' href='$theme_path/css/summary-table.css' rel='stylesheet'>
<link type='text/css' href='$theme_path/css/theme.css' rel='stylesheet'>
$theme_extras
<!-- Theme Javascript -->
<script type='text/javascript' src='$theme_path/js/jquery-ui-1.8.22.custom.min.js'></script>
<!--[if lt IE 9]><script type='text/javascript' src='$theme_path/js/jqplot/excanvas.min.js'></script><![endif]-->
<script type='text/javascript' src='$theme_path/js/jqplot/jquery.jqplot.min.js'></script>
<script type='text/javascript' src='$theme_path/js/jqplot/plugins/jqplot.barRenderer.min.js'></script>
<script type='text/javascript' src='$theme_path/js/jqplot/plugins/jqplot.pieRenderer.min.js'></script>
<script type='text/javascript' src='$theme_path/js/jqplot/plugins/jqplot.dateAxisRenderer.min.js'></script>
<script type='text/javascript' src='$theme_path/js/jqplot/plugins/jqplot.categoryAxisRenderer.min.js'></script>
<script type='text/javascript' src='$theme_path/js/jqplot/plugins/jqplot.canvasAxisLabelRenderer.min.js'></script>
<script type='text/javascript' src='$theme_path/js/jqplot/plugins/jqplot.canvasAxisTickRenderer.min.js'></script>
<script type='text/javascript' src='$theme_path/js/jqplot/plugins/jqplot.canvasTextRenderer.min.js'></script>
<script type='text/javascript' src='$theme_path/js/jqplot/plugins/jqplot.pointLabels.min.js'></script>
<script type='text/javascript' src='$theme_path/js/jqplot/plugins/jqplot.highlighter.min.js'></script>
<script type='text/javascript' src='$theme_path/js/jquery.dataTables.min.js'></script>
<script type='text/javascript' src='$theme_path/js/jquery.lightbox-0.5.min.js'></script>
<script type='text/javascript' src='$theme_path/js/superfish.js'></script>
<script type='text/javascript' src='$theme_path/js/jquery-tools-tooltip-1.2.7.js'></script>
<script type='text/javascript' src='$theme_path/js/theme.js'></script>

";
}
